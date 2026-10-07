# Harvestability Engine

The harvestability layer combines perception confidence, 3D localization confidence, ripeness evidence, reachability, collision clearance, sensor quality, occlusion, and temporal tracking stability.

It returns explicit abstention states including LOW_CONFIDENCE, TARGET_OCCLUDED, NOT_REACHABLE, COLLISION_RISK, SENSOR_FAILURE, HUMAN_REVIEW, and UNKNOWN.

A high score is only a candidate for the next validation stage. It never authorizes physical actuation by itself.