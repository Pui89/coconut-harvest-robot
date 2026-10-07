# Embodied AI Architecture — Gemma 4 31B IT

```mermaid
flowchart LR
A[RGB-D + LiDAR] --> B[Vision / Segmentation]
B --> C[3D World Model]
C --> D[Gemma 4 31B IT\nMultimodal Reasoning]
D --> E[Task / VLA Candidate Actions]
E --> F[Deterministic Safety Gate]
F --> G[ROS 2 / MoveIt 2]
G --> H[Mobile Base + 6-DOF Arm + Cutter]
H --> I[Vision + Force Verification]
I --> C
```

Gemma is advisory only. Candidate actions must pass workspace, collision, exclusion-zone, joint-limit, velocity/force and emergency-stop checks before hardware execution.

Model reference: https://huggingface.co/google/gemma-4-31B-it
