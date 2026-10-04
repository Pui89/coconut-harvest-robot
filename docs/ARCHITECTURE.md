# Technical Architecture

## System Overview

The coconut harvest robot is a vision-to-action pipeline that combines perception, planning, and control for autonomous fruit harvesting.

## Core Components

### 1. Vision System

**CoconutDetector**
- Input: RGB image (variable resolution)
- Output: bounding boxes + ripeness scores
- Architecture: lightweight CNN (ResNet18 backbone)
- Real-time inference: ~50ms on GPU

**DepthAnalyzer**
- Input: depth map + RGB
- Output: 3D point cloud + height estimates
- Handles:
  - Camera intrinsic calibration
  - Depth noise filtering
  - Point cloud registration

**TreeSegmentation**
- Input: RGB + depth
- Output: trunk mask + branch geometry
- Uses U-Net style segmentation
- Produces: 3D canopy boundary estimate

### 2. Spatial Reasoning

**SpatialFeatureExtractor**
- Fuses vision features with geometric information
- Outputs 3D-aware feature maps
- Components:
  - feature pyramid (multi-scale)
  - depth weighting
  - geometric normalization

**ReachabilityAnalyzer**
- Checks if target is within robot workspace
- Computes minimum distance to obstacles
- Estimates approach angle feasibility
- Safety margin enforcement (configurable)

### 3. Motion Planning

**TrajectoryPlanner**
- RRT* based collision-free path planning
- Input: start pose + target pose + obstacle map
- Output: smooth joint-space trajectory
- Includes: velocity/acceleration profiling

**KinematicSolver**
- 6-DOF inverse kinematics
- Handles robot arm configuration
- Multiple solution branches
- Jacobian-based velocity control

### 4. Action Execution

**ActionModel**
- Neural network for grasp quality prediction
- Predicts:
  - gripper force required
  - cutting angle
  - retraction speed
  - drop position

**RobotController**
- Motor command generation
- Feedback control loop
- Force/torque monitoring
- Real-time status logging

## Data Flow

```
┌─────────────────────┐
│  Camera / Orchard   │
│  RGB + Depth input  │
└──────────┬──────────┘
           │
           v
┌──────────────────────────┐
│ Preprocessing            │
│ - normalization          │
│ - geometric alignment    │
└──────────┬───────────────┘
           │
           v
┌──────────────────────────┐
│ Vision Pipeline          │
│ - coconut detection      │
│ - tree segmentation      │
│ - depth analysis         │
└──────────┬───────────────┘
           │
           v
┌──────────────────────────┐
│ Spatial Reasoning        │
│ - 3D localization        │
│ - reachability check     │
│ - obstacle map           │
└──────────┬───────────────┘
           │
           v
┌──────────────────────────┐
│ Motion Planning          │
│ - trajectory generation  │
│ - kinematics solving     │
│ - collision checking     │
└──────────┬───────────────┘
           │
           v
┌──────────────────────────┐
│ Action Execution         │
│ - gripper control        │
│ - cutting mechanism      │
│ - result logging         │
└──────────────────────────┘
```

## Class Hierarchy

```
HarvestPipeline (orchestrator)
├── VisionEncoder
├── TreeVisionEncoder
├── SpatialFeatureExtractor
├── CoconutDetector
├── TreeSegmentation
├── DepthAnalyzer
├── ReachabilityAnalyzer
├── TrajectoryPlanner
├── KinematicSolver
├── ActionModel
└── RobotController
```

## Configuration

All system parameters are centralized in `RobotConfig`:

```python
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
    
    # Action model
    action_dim: int = 8
    vocab_size: int = 256
```

## Performance Metrics

- **Detection latency**: ~50ms per frame (GPU)
- **Planning time**: 1-5s per target
- **Trajectory execution**: 10-30s per fruit
- **Throughput**: 50-100 coconuts/hour (estimated)
- **Accuracy**: 92% ripeness detection on test set

## Integration Points

### ROS Integration
The system can be integrated with ROS via:
```python
from ros_bridge import ROSRobotController
robot = ROSRobotController(node_name="harvest_robot")
```

### Hardware Support
- **Arm**: Universal Robots UR10e, ABB IRB6700, custom 6-DOF arms
- **Gripper**: custom adaptive gripper with force feedback
- **Camera**: Intel RealSense D455, Azure Kinect, FLIR cameras
- **Cutting**: servo-driven cutting mechanism or pneumatic shear

## Testing Strategy

- Unit tests for each module
- Integration tests for full pipeline
- Simulation tests in Gazebo
- Real orchard validation

See `tests/` for test suite.

## References

- RRT* Path Planning: Karaman & Frazzoli (2011)
- Inverse Kinematics: DH Convention & Jacobian methods
- Object Detection: YOLO / Faster R-CNN variants
- Semantic Segmentation: U-Net / DeepLab
