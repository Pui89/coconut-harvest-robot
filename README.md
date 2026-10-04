# Coconut Harvest Robot

A PyTorch-based robotic agriculture project for coconut harvesting in high trees. The system combines:

- vision-based coconut and tree detection
- depth or height estimation
- spatial feature extraction for canopy understanding
- action planning for robot arm or harvesting mechanism
- clean object-oriented code for agriculture robotics research and prototyping

## Project goals

This project is designed to support a robotic system that can:

- identify coconut clusters on tall trees
- estimate trunk and branch height
- localize reachable fruit positions in 3D space
- generate safe harvesting trajectories
- manage multi-step action planning for removal or cutting

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── pyproject.toml
├── demo.py
├── src
│   └── coconut_harvest_robot
│       ├── __init__.py
│       ├── config.py
│       ├── data.py
│       ├── vision.py
│       ├── spatial.py
│       ├── planner.py
│       ├── action_model.py
│       ├── pipeline.py
│       └── utils.py
└── tests
    └── test_pipeline.py
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Quick start

```bash
python demo.py
```

## Example usage

```python
import torch
from coconut_harvest_robot.pipeline import HarvestPipeline

pipeline = HarvestPipeline()
rgb = torch.rand(1, 3, 128, 128)
depth = torch.rand(1, 1, 128, 128)

result = pipeline(rgb, depth, "harvest ripe coconut on the upper right side")
print(result.scene_repr.shape)
print(result.spatial_features.shape)
print(result.action_plan)
```

## Future extensions

- Replace synthetic data with real farm camera feeds
- Integrate point cloud depth estimation from stereo or LiDAR
- Add arm trajectory optimization for safe cutting
- Use vision-language grounding to identify ripe coconuts
- Develop autonomous orchard navigation and field path planning

## License

MIT
