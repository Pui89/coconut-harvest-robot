# Executable end-to-end harvest mission reference

This adds a runnable software vertical slice: structured sensor-health inputs -> fail-closed validation -> target/ripeness gate -> reach/point-obstacle checks -> deterministic target selection -> reviewable plan -> integrity digest -> tests/CI.

## Run

```bash
python -m unittest discover -s tests -p 'test_e2e_harvest.py' -v
python -m e2e_harvest.mission --input examples/harvest_mission.json --output harvest-report.json
```

The example data is synthetic. The obstacle check is point-distance screening, **not** a full robot/arm collision model. The integrity digest detects accidental report changes; it is not a signature or proof of origin.

## Safety and integration boundary

Every report sets `human_review_required=true`, `actuator_authorized=false`, and `execution_mode=SIMULATION_ONLY`. There is no ROS 2 publisher or motor interface in this reference. To approach physical deployment, add calibrated camera/depth/LiDAR drivers, timestamp synchronization, TF2 frame transforms, validated fruit segmentation/tracking, robot URDF/SRDF and MoveIt 2 collision checking, hardware E-stop and safety-rated controller integration, watchdogs, force/torque limits, and supervised low-speed tests. A software boolean is not a substitute for a safety-rated E-stop.

## Benchmarks to report (not pre-claimed)

On a fixed, versioned orchard dataset and hardware configuration, report target precision/recall and AP, 3D localization error, ripeness calibration, collision-check false negatives, plan success, cycle time, energy per harvested fruit, damage rate, and abstention rate. Include confidence intervals, weather/lighting strata, unseen-orchard tests, and failure-injection tests. Do not publish fabricated benchmark values.
