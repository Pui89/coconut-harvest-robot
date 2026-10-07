# Evaluation Benchmark

Measure before claiming autonomy.

| Area | Metrics |
|---|---|
| Detection | precision, recall, F1, mAP50, mAP50-95 |
| Segmentation | IoU, boundary quality |
| Tracking | IDF1, HOTA, track stability |
| 3D | depth MAE, 3D localization error |
| Harvestability | calibration, abstention rate, false-harvest rate |
| Planning | success rate, path length, planning time |
| Robotics | harvest success, failed harvest, collision rate, cycle time, energy/tree |
| Safety | unsafe-action rate, E-stop response, human-detection failure, sensor-failure recovery |
| Operations | uptime, battery consumption, maintenance time, cost/tree |

Evaluate across lighting, weather, canopy density, distance, occlusion, tree height, sensor configuration and hardware profile. Record dataset/model provenance and confidence intervals where possible.