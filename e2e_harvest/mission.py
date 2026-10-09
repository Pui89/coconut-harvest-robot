"""Deterministic, simulation-only end-to-end harvest mission reference."""
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path
from typing import Any

def _digest(value: dict[str, Any]) -> str:
    clean = dict(value)
    clean.pop("integrity_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()

def run_mission(m: dict[str, Any]) -> dict[str, Any]:
    """Validate observations -> target selection -> reachability -> reviewable plan.

    This reference never actuates hardware. Inputs are measurements/proposals, not trusted commands.
    """
    if not isinstance(m, dict) or not isinstance(m.get("mission_id"), str) or not m["mission_id"].strip():
        raise ValueError("mission_id must be a non-empty string")
    health = m.get("sensor_health", {})
    if not isinstance(health, dict) or not health or any(v is not True for v in health.values()):
        status, reason, target, plan = "ABSTAIN", "SENSOR_HEALTH_GATE_FAILED", None, []
    elif m.get("emergency_stop") is True:
        status, reason, target, plan = "ABSTAIN", "EMERGENCY_STOP_ACTIVE", None, []
    else:
        cfg = m.get("workspace", {})
        reach = cfg.get("max_reach_m", 0) if isinstance(cfg, dict) else 0
        if not isinstance(reach, (int, float)) or isinstance(reach, bool) or not math.isfinite(reach) or reach <= 0:
            raise ValueError("workspace.max_reach_m must be a positive finite number")
        obstacles = m.get("obstacle_points_m", [])
        if not isinstance(obstacles, list):
            raise ValueError("obstacle_points_m must be a list")
        for p in obstacles:
            if not (isinstance(p, list) and len(p) == 3 and all(isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) for x in p)):
                raise ValueError("each obstacle point must be a finite [x,y,z]")
        candidates = m.get("candidates", [])
        if not isinstance(candidates, list):
            raise ValueError("candidates must be a list")
        valid = []
        for c in candidates:
            if not isinstance(c, dict) or not isinstance(c.get("target_id"), str):
                raise ValueError("each candidate requires target_id")
            xyz = c.get("position_m")
            score = c.get("ripeness_score")
            if not (isinstance(xyz, list) and len(xyz) == 3 and all(isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) for x in xyz)):
                raise ValueError("candidate position_m must be finite [x,y,z]")
            if not isinstance(score, (int, float)) or isinstance(score, bool) or not math.isfinite(score) or not 0 <= score <= 1:
                raise ValueError("ripeness_score must be between 0 and 1")
            distance = math.sqrt(sum(float(x)**2 for x in xyz))
            if distance > reach:
                continue
            # Conservative point-obstacle exclusion radius. Real deployments need robot-volume collision checking.
            if any(math.dist(xyz, p) < float(m.get("obstacle_clearance_m", 0.25)) for p in obstacles):
                continue
            if score >= float(m.get("minimum_ripeness_score", 0.7)):
                valid.append((float(score), c["target_id"], xyz))
        if not valid:
            status, reason, target, plan = "NO_SAFE_TARGET", "NO_CANDIDATE_PASSED_GATES", None, []
        else:
            score, target_id, xyz = sorted(valid, key=lambda x: (-x[0], x[1]))[0]
            status, reason = "PLAN_READY_FOR_HUMAN_REVIEW", "TARGET_PASSED_REFERENCE_GATES"
            target = {"target_id": target_id, "position_m": [float(x) for x in xyz], "ripeness_score": score}
            plan = [{"step": "APPROACH", "target_id": target_id}, {"step": "HARVEST_PROPOSAL", "target_id": target_id}, {"step": "RETRACT", "target_id": target_id}]
    report = {"schema_version": "1.0", "mission_id": m["mission_id"], "status": status, "reason": reason,
              "selected_target": target, "plan": plan, "human_review_required": True,
              "actuator_authorized": False, "execution_mode": "SIMULATION_ONLY"}
    report["integrity_sha256"] = _digest(report)
    return report

def verify_report(report: dict[str, Any]) -> bool:
    return isinstance(report, dict) and isinstance(report.get("integrity_sha256"), str) and report["integrity_sha256"] == _digest(report)

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    mission = json.loads(Path(args.input).read_text(encoding="utf-8"))
    report = run_mission(mission)
    Path(args.output).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "output": args.output, "integrity_ok": verify_report(report)}))
if __name__ == "__main__":
    main()
