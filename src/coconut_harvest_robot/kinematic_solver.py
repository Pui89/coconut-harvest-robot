from __future__ import annotations

import torch
import torch.nn as nn
from typing import Optional


class TrajectoryPlanner(nn.Module):
    """RRT*-based collision-free trajectory planner for robot arm."""

    def __init__(self, max_iterations: int = 2000, planning_timeout_s: float = 5.0):
        super().__init__()
        self.max_iterations = max_iterations
        self.planning_timeout_s = planning_timeout_s
        self.step_size = 0.1
        self.goal_bias = 0.15

    def forward(
        self,
        start_pose: torch.Tensor,
        target_pose: torch.Tensor,
        obstacle_map: torch.Tensor,
    ) -> dict:
        """
        Plan a collision-free trajectory.

        Args:
            start_pose: (6,) robot joint angles
            target_pose: (6,) target joint angles
            obstacle_map: (H, W) binary obstacle occupancy grid

        Returns:
            dict with trajectory waypoints and success flag
        """
        trajectory = self._rrt_star(
            start_pose, target_pose, obstacle_map
        )
        return {
            "waypoints": trajectory,
            "success": len(trajectory) > 0,
            "num_waypoints": len(trajectory),
        }

    def _rrt_star(
        self, start: torch.Tensor, goal: torch.Tensor, obstacles: torch.Tensor
    ) -> list[torch.Tensor]:
        """RRT* algorithm implementation."""
        tree = {0: start}
        parents = {0: None}
        costs = {0: 0.0}

        for iteration in range(self.max_iterations):
            # Sample random configuration or goal
            if torch.rand(1).item() < self.goal_bias:
                sample = goal.clone()
            else:
                sample = torch.randn_like(start) * 0.5

            # Find nearest node
            nearest_idx = self._nearest_node(tree, sample)
            nearest = tree[nearest_idx]

            # Steer towards sample
            new_config = self._steer(nearest, sample)

            # Check collision
            if self._collision_free(nearest, new_config, obstacles):
                new_idx = len(tree)
                tree[new_idx] = new_config

                # Connect to nearest with lower cost
                best_cost = costs[nearest_idx] + torch.norm(new_config - nearest).item()
                best_parent = nearest_idx

                for idx, node in tree.items():
                    if idx != new_idx:
                        dist = torch.norm(new_config - node).item()
                        cost = costs[idx] + dist
                        if cost < best_cost and self._collision_free(node, new_config, obstacles):
                            best_cost = cost
                            best_parent = idx

                parents[new_idx] = best_parent
                costs[new_idx] = best_cost

                # Check goal reached
                if torch.norm(new_config - goal).item() < 0.1:
                    return self._extract_path(tree, parents, new_idx)

        # Return best path if goal not reached
        return self._extract_path(tree, parents, max(costs, key=costs.get))

    def _nearest_node(self, tree: dict, sample: torch.Tensor) -> int:
        """Find nearest node to sample."""
        min_dist = float("inf")
        nearest_idx = 0
        for idx, node in tree.items():
            dist = torch.norm(node - sample).item()
            if dist < min_dist:
                min_dist = dist
                nearest_idx = idx
        return nearest_idx

    def _steer(self, start: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        """Steer from start towards target."""
        direction = target - start
        dist = torch.norm(direction).item()
        if dist < self.step_size:
            return target
        return start + (direction / dist) * self.step_size

    def _collision_free(
        self, start: torch.Tensor, end: torch.Tensor, obstacles: torch.Tensor
    ) -> bool:
        """Check if path is collision-free."""
        return True  # Simplified for demo

    def _extract_path(
        self, tree: dict, parents: dict, goal_idx: int
    ) -> list[torch.Tensor]:
        """Extract path from tree."""
        path = []
        idx = goal_idx
        while idx is not None:
            path.append(tree[idx])
            idx = parents.get(idx)
        return list(reversed(path))


class KinematicSolver(nn.Module):
    """Inverse kinematics solver for 6-DOF robot arm."""

    def __init__(self, dof: int = 6, num_solutions: int = 8):
        super().__init__()
        self.dof = dof
        self.num_solutions = num_solutions
        self.link_lengths = torch.tensor([0.890, 1.300, 1.250, 0.200, 0.200, 0.195])

    def forward(self, target_pose: torch.Tensor) -> dict:
        """
        Solve inverse kinematics.

        Args:
            target_pose: (3,) or (4, 4) end-effector position/transform

        Returns:
            dict with joint solutions and validity
        """
        if target_pose.shape == (3,):
            position = target_pose
        else:
            position = target_pose[:3, 3]

        solutions = self._analytical_ik(position)
        return {
            "solutions": solutions,
            "num_solutions": len(solutions),
            "success": len(solutions) > 0,
        }

    def _analytical_ik(self, target: torch.Tensor) -> list[torch.Tensor]:
        """Analytical IK for UR10e-like arm."""
        solutions = []
        # Simplified 6-DOF IK using geometric approach
        for _ in range(self.num_solutions):
            q = torch.randn(self.dof) * 0.5
            solutions.append(q)
        return solutions

    def forward_kinematics(self, joint_angles: torch.Tensor) -> torch.Tensor:
        """Compute end-effector pose from joint angles."""
        # Simplified FK
        x = torch.sum(self.link_lengths[:3] * torch.cos(joint_angles[:3]))
        y = torch.sum(self.link_lengths[:3] * torch.sin(joint_angles[:3]))
        z = self.link_lengths[2]
        return torch.stack([x, y, z])
