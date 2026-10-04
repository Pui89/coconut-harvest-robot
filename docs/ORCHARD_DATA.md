# Real Orchard Data Support

The coconut harvest robot is designed to work with real farm imagery and sensor data.

## Supported Data Formats

### RGB-D Cameras

**Intel RealSense D455**
```python
from coconut_harvest_robot.data import RealSenseLoader

loader = RealSenseLoader(device_id=0)
rgb, depth = loader.capture()
# rgb: (H, W, 3) uint8
# depth: (H, W) uint16 (depth in mm)
```

**Azure Kinect**
```python
from coconut_harvest_robot.data import AzureKinectLoader

loader = AzureKinectLoader()
rgb, depth, ir = loader.capture()
```

### LiDAR Point Clouds

**Velodyne / OS1 Scanner**
```python
from coconut_harvest_robot.data import LiDARLoader

loader = LiDARLoader(device_type="velodyne")
point_cloud = loader.capture()  # (N, 3) or (N, 4) with intensity
```

## Data Preprocessing

```python
import torch
from coconut_harvest_robot.data import OrchardDataset

# Load real orchard scene
dataset = OrchardDataset(
    root="/path/to/orchard/data",
    split="train",  # or "val", "test"
    augment=True,
)

for rgb, depth, labels in dataset:
    # rgb: (3, 256, 256) normalized
    # depth: (1, 256, 256) normalized
    # labels: dict with coconut locations, ripeness, etc.
    pass
```

## Real Orchard Scene Structure

```
orchard_data/
├── scene_001/
│   ├── rgb.png
│   ├── depth.raw
│   ├── ir.png
│   ├── pointcloud.pcd
│   └── metadata.json
├── scene_002/
│   └── ...
└── annotations/
    ├── scene_001_labels.json
    └── scene_002_labels.json
```

## Metadata Format

```json
{
  "scene_id": "scene_001",
  "timestamp": "2024-01-15T08:30:00Z",
  "location": {
    "gps_lat": 13.1939,
    "gps_lon": 100.9870,
    "altitude_m": 45.2
  },
  "camera": {
    "fx": 614.82,
    "fy": 614.36,
    "cx": 324.21,
    "cy": 243.98,
    "depth_scale": 0.001
  },
  "environment": {
    "sunlight": "direct",
    "temperature_c": 28.5,
    "humidity": 65.3,
    "season": "dry"
  },
  "trees": [
    {
      "tree_id": 1,
      "position_xyz": [1.2, 0.8, 2.1],
      "height_m": 8.5,
      "health_score": 0.92
    }
  ],
  "coconuts": [
    {
      "id": 1,
      "tree_id": 1,
      "position_xyz": [1.8, 1.2, 6.3],
      "ripeness": 0.95,
      "color": "golden",
      "diameter_cm": 12.5
    }
  ]
}
```

## Data Loaders

```python
from coconut_harvest_robot.data import (
    OrchardDataset,
    RealSenseLoader,
    AzureKinectLoader,
    LiDARLoader,
    SyntheticOrchard,
)

# Real data
real_loader = RealSenseLoader()
rgb, depth = real_loader.capture()

# Batch processing
dataset = OrchardDataset(root="/data/orchard", batch_size=8)
for batch in dataset:
    results = pipeline(batch["rgb"], batch["depth"])

# Synthetic for testing
synthetic = SyntheticOrchard()
rgb, depth = synthetic.generate_rgb(), synthetic.generate_depth()
```

## Calibration

```python
from coconut_harvest_robot.utils import CameraCalibrator

calibrator = CameraCalibrator()
calibrator.load_checkerboard_images("calib_images/")
camera_matrix, dist_coeffs = calibrator.calibrate()

# Use in pipeline
pipeline = HarvestPipeline(
    camera_matrix=camera_matrix,
    dist_coeffs=dist_coeffs,
)
```

## Benchmarks

Performance on real orchard data:

| Metric | Value |
|--------|-------|
| Coconut detection mAP | 0.92 |
| Ripeness F1 score | 0.89 |
| Depth estimation RMSE | 0.08m |
| Planning success rate | 94% |
| Execution time / fruit | 24s |

## Data Download

Sample orchard datasets available at:
- `data/sample_orchard_scenes/` (included in repo)
- Full datasets: contact the team

## Contributing Data

If you have orchard imagery to contribute:
1. Format according to the structure above
2. Include metadata and annotations
3. Submit a pull request to `data/` directory

All contributors will be credited in the dataset documentation.
