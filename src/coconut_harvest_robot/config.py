from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RobotConfig:
    # Image processing
    image_size: tuple[int, int] = (256, 256)
    depth_scale: float = 1000.0  # mm per depth unit

    # Robot specs
    arm_reach_m: float = 2.8
    arm_dof: int = 6
    max_height_m: float = 14.0

    # End effector
    gripper_force_n: float = 150.0
    cutting_force_n: float = 500.0

    # Planning
    planning_timeout_s: float = 5.0
    rrt_iterations: int = 2000
    safety_margin_m: float = 0.15

    # Model dims
    hidden_dim: int = 32
    spatial_dim: int = 16
    action_dim: int = 8
    vocab_size: int = 256
