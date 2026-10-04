import torch

from coconut_harvest_robot.pipeline import HarvestPipeline


def test_pipeline_generates_outputs():
    pipeline = HarvestPipeline()
    rgb = torch.rand(1, 3, 128, 128)
    depth = torch.rand(1, 1, 128, 128)

    result = pipeline(rgb, depth, "harvest ripe coconut on the upper right side")

    assert result.scene_repr.shape[0] == 1
    assert result.spatial_features.shape[0] == 1
    assert result.action_logits.shape[0] == 1
    assert result.action_plan["status"] == "planned"
