# Multimodal AI Narcotics Detection

The existing robot perception stack is extended as a defensive, evidence-oriented screening system for suspected controlled substances.

## Detection taxonomy
- amphetamine
- heroin
- methamphetamine crystal
- narcotic unknown
- unknown substance

An unknown object is never automatically classified as a drug, and a missing detection is not proof of absence.

## Full AI stack

RGB/RGB-D/thermal/NIR/LiDAR -> YOLO -> SAM3 -> tracking + 3D fusion -> anomaly/unknown screening -> Qwen3-VL -> Gemma4-E4B secondary review -> V-JEPA2 prediction -> human review -> optional safe camera repositioning.

Existing action candidates (GR00T N1.7, FLUX 3 Action, SmolVLA, OpenVLA and pi0) are restricted to observation/camera-reposition proposals. They never receive direct motor authority.

## Simulation and datasets
Isaac Sim / Isaac Lab provide controlled simulation. LTX-2.5-Diffusers and MiniMax H3 Turbo LoRA can generate difficult scenarios offline. LeRobot can organize demonstrations and evaluation datasets. Synthetic data requires provenance and license review.

Generated imagery is not forensic ground truth. Validate against independently collected, legally obtained benchmark data.

## Safety
This is a screening aid, not a forensic identification instrument. Visual AI cannot reliably establish chemical identity from appearance alone. High-consequence decisions require qualified human review and, where applicable, validated analytical testing.

The robot must not seize, open, crush, consume, or chemically manipulate suspected substances; autonomously make enforcement decisions; declare legal confirmation from vision alone; or bypass human review.

Recommended states: UNKNOWN, SUSPECTED_SUBSTANCE, HUMAN_REVIEW.
