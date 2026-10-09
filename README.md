# Coconut Harvest Robot


## PUI89 AI Robotics Platform

**Autonomous multimodal embodied-AI platform for orchard harvesting.**

This repository is one vertical implementation of the **PUI89 AI Robotics** platform for agriculture. The common architecture is:

```text
Multimodal Sensors
      ↓
Quality / Health Gate
      ↓
Perception + Tracking
      ↓
3D / 4D World Model
      ↓
Uncertainty + OOD
      ↓
Foundation-Model Reasoning
      ↓
Task Planning
      ↓
Deterministic Safety Supervisor
      ↓
ROS 2 / Robot Control
      ↓
Telemetry / Evidence
      ↓
MLOps / Fleet Learning
```

### Executable end-to-end reference

- [E2E Harvest Mission: run instructions, safety boundaries and benchmark plan](docs/E2E_HARVEST_MISSION.md)
- [Synthetic mission input](examples/harvest_mission.json)
- [Runnable mission pipeline](e2e_harvest/mission.py)
- [Automated tests](tests/test_e2e_harvest.py)
- [Python 3.10–3.12 CI workflow](.github/workflows/e2e-harvest.yml)

This vertical slice validates sensor health, target/ripeness gates, reachability and point-obstacle checks, then emits a reviewable plan. It is simulation-only and never authorizes actuators. It does not replace calibrated perception, full robot-volume collision checking, ROS 2/MoveIt integration, or safety-rated hardware validation.

### Product tiers

- **PUI89 Research** — universities, robotics competitions, researchers
- **PUI89 Professional** — farms, plantations, agricultural operators
- **PUI89 Enterprise** — large corporations, governments, logistics, ports, infrastructure

### Cross-environment research

The same perception/world-model/uncertainty/safety interfaces are designed to transfer between agriculture, disaster response and security/inspection. Transfer must be measured with the repository benchmark; it is not assumed from architecture alone.

- [Optional DINOv2 + Anomalib integration, end-to-end verification and tests](docs/OPEN_SOURCE_VISION_INTEGRATION.md)

### Evidence standard

This project separates **targets, prototypes and measured results**. Production or field-validation claims require reproducible benchmark evidence, failure testing, and documented safety validation.

See:
- [PUI89 Benchmark](docs/PUI89_BENCHMARK.md)
- [Cross-Environment Transfer Benchmark](docs/PUI89_TRANSFER_BENCHMARK.md)
- [Product Tiers](docs/PUI89_PRODUCT_TIERS.md)
- [Failure and UNKNOWN Protocol](docs/PUI89_FAILURE_AND_UNKNOWN_PROTOCOL.md)
- [MLOps Model Lifecycle](docs/PUI89_MLOPS_MODEL_LIFECYCLE.md)
- [Research, Competition and Commercial Evidence](docs/PUI89_RESEARCH_COMPETITION_INVESTOR.md)
- [12-Month Roadmap](docs/PUI89_12_MONTH_ROADMAP.md)

A PyTorch-based robotic agriculture system for autonomous coconut harvesting in high trees. Combines vision-based fruit detection, 3D spatial reasoning, trajectory planning, and action execution in a production-ready framework.

![Coconut harvest robot concept](docs/images/coconut_harvest_robot_photo.svg)

## 3D / 4D Realistic Robot Concept

![Realistic 3D/4D coconut harvest robot](docs/coconut_harvest_robot_3d_4d_concept.svg)

A new concept render presents the autonomous orchard platform with RGB-D/LiDAR sensing, sensor mast, mobile chassis, articulated harvesting arm, coconut target tracking, and a time-aware 4D trajectory visualization.

- **3D/4D concept:** `docs/coconut_harvest_robot_3d_4d_concept.svg`
- **4D demo video:** `docs/coconut_harvest_robot_4d_demo.mp4`

The SVG contains an animated target trajectory to visualize the fourth dimension (time). The MP4 is a lightweight preview of the robot's arm tracking motion.
