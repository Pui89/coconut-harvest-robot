import json, subprocess, sys, tempfile, unittest
from pathlib import Path
from e2e_harvest.mission import run_mission, verify_report

ROOT = Path(__file__).resolve().parents[1]
def sample():
    return json.loads((ROOT / "examples/harvest_mission.json").read_text())

class HarvestE2ETests(unittest.TestCase):
    def test_sample_routes_to_review_not_actuation(self):
        r = run_mission(sample())
        self.assertEqual(r["status"], "PLAN_READY_FOR_HUMAN_REVIEW")
        self.assertTrue(r["human_review_required"])
        self.assertFalse(r["actuator_authorized"])
        self.assertEqual(r["execution_mode"], "SIMULATION_ONLY")
        self.assertTrue(verify_report(r))
    def test_bad_sensor_fails_closed(self):
        m = sample(); m["sensor_health"]["depth"] = False
        r = run_mission(m)
        self.assertEqual(r["status"], "ABSTAIN")
        self.assertIsNone(r["selected_target"])
    def test_estop_fails_closed(self):
        m = sample(); m["emergency_stop"] = True
        self.assertEqual(run_mission(m)["reason"], "EMERGENCY_STOP_ACTIVE")
    def test_out_of_reach_target_rejected(self):
        m = sample(); m["candidates"][0]["position_m"] = [20, 0, 0]
        self.assertEqual(run_mission(m)["status"], "NO_SAFE_TARGET")
    def test_obstacle_clearance_rejects_target(self):
        m = sample(); m["obstacle_points_m"] = [m["candidates"][0]["position_m"]]
        self.assertEqual(run_mission(m)["status"], "NO_SAFE_TARGET")
    def test_unripe_target_rejected(self):
        m = sample(); m["candidates"][0]["ripeness_score"] = 0.1
        self.assertEqual(run_mission(m)["status"], "NO_SAFE_TARGET")
    def test_tamper_detected(self):
        r = run_mission(sample()); r["status"] = "ACTUATE"
        self.assertFalse(verify_report(r))
    def test_invalid_candidate_rejected(self):
        m = sample(); m["candidates"][0]["position_m"] = [float("nan"), 0, 0]
        with self.assertRaises(ValueError): run_mission(m)
    def test_cli(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "report.json"
            subprocess.run([sys.executable, "-m", "e2e_harvest.mission", "--input", str(ROOT/"examples/harvest_mission.json"), "--output", str(out)], check=True, cwd=ROOT, capture_output=True, text=True)
            self.assertTrue(verify_report(json.loads(out.read_text())))
if __name__ == "__main__": unittest.main()
