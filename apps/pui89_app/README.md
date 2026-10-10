# PUI89 Coconut Harvest AI Application

A simulation-first FastAPI service for coconut harvest **decision support**. It accepts structured perception evidence, applies explicit quality/uncertainty/safety gates, and returns auditable proposals. It does not run a trained detector by itself and never commands physical actuators.

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r apps/pui89_app/requirements.txt
uvicorn apps.pui89_app.main:app --reload
```
Open `http://127.0.0.1:8000/docs` for the API schema and interactive requests.

## API
- `GET /health` — service status and actuator boundary.
- `POST /analyze` — sensor quality checks, candidate ranking and gated harvest proposals.
- `GET /metrics` — process-level request counters; not a model benchmark.

Example JSON:
```json
{
  "rgb_available": true,
  "depth_valid": true,
  "timestamp_skew_ms": 8,
  "candidates": [{
    "target_id": "coconut-01",
    "ripeness_score": 0.91,
    "localization_confidence": 0.94,
    "distance_m": 2.1,
    "obstacle_clearance_m": 0.45,
    "stable_track_frames": 12
  }]
}
```

## Safety and evidence
- Missing/degraded inputs or excessive timestamp skew trigger `SAFE_HOLD`.
- Candidates failing confidence, tracking, reachability or clearance gates are rejected or sent for review.
- `PROPOSAL_APPROVED_NOT_EXECUTED` means only that this software's configured gates passed; it is not authorization to move a robot.
- No trained model, real orchard accuracy, throughput or safety certification is claimed.
- Evaluate on held-out orchard data and report precision/recall, localization error, end-to-end latency, memory, abstention, failure cases and simulation-vs-field results separately.

## Tests
```bash
python -m unittest discover -s apps/pui89_app -p 'test_*.py' -v
```
