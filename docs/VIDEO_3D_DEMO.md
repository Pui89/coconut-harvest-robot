# 3D Working Robot Demo

This repository now contains a reproducible 3D coconut-harvesting robot visualization pipeline.

## Generate

```bash
pip install numpy matplotlib trimesh imageio
python sim/coconut_harvester_demo.py
```

The script generates:
- `sim/assets/coconut_harvester_3d.glb` — a portable 3D robot/orchard scene.
- `sim/assets/coconut_harvester_demo.mp4` — animated drive/scan/approach/cut/verify/retract demonstration.

The robot is based on the concrete URDF in `robots/coconut_harvester.urdf`. For physics-backed execution, load that URDF into Isaac Sim or Gazebo/ROS 2 and connect the existing planner and deterministic safety gate.

The MP4 is a rendered demonstration, not evidence of physical hardware performance.
