from coconut_harvest_robot.harvestability import HarvestDecision,HarvestEvidence,score_harvestability
from coconut_harvest_robot.safety_gate import ActionCandidate,SafetyDecision,validate_action

def test_low_confidence_abstains():
    r=score_harvestability(HarvestEvidence(.5,.5,.5,.5,.5,sensor_quality=.8))
    assert r.decision==HarvestDecision.LOW_CONFIDENCE

def test_safety_blocks_human_exclusion():
    r=validate_action(ActionCandidate("c1",.95,.5,.1,100,5,human_in_exclusion_zone=True))
    assert r.decision==SafetyDecision.BLOCK

def test_safety_approves_safe_candidate():
    r=validate_action(ActionCandidate("c1",.95,.5,.1,100,5))
    assert r.decision==SafetyDecision.APPROVE
