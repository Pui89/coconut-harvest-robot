from __future__ import annotations

import torch

from coconut_harvest_robot.pipeline import HarvestPipeline


def main() -> None:
    pipeline = HarvestPipeline()
    rgb = torch.rand(1, 3, 128, 128)
    depth = torch.rand(1, 1, 128, 128)

    result = pipeline(rgb, depth, "harvest ripe coconut on the upper right side")
    print("scene_repr:", tuple(result.scene_repr.shape))
    print("spatial_features:", tuple(result.spatial_features.shape))
    print("action_plan:", result.action_plan)
    print("harvest_pose:", result.harvest_pose)


if __name__ == "__main__":
    main()
