from coconut_harvest_robot.narcotics_detection import NarcoticsScreeningPipeline


def test_unknown_when_no_confident_detection():
    result = NarcoticsScreeningPipeline().screen({"frame_id": "test"})
    assert result.state == "UNKNOWN"
    assert result.requires_human_review


def test_unrecognized_label_is_unknown():
    pipeline = NarcoticsScreeningPipeline(detector=lambda _: [{"label": "something_else", "confidence": 0.95}])
    result = pipeline.screen({"frame_id": "test"})
    assert result.candidates[0].label == "unknown_substance"
    assert result.state == "HUMAN_REVIEW"


def test_candidate_requires_human_review():
    pipeline = NarcoticsScreeningPipeline(detector=lambda _: [{"label": "methamphetamine_crystal", "confidence": 0.91, "evidence": ["visual_candidate"]}])
    result = pipeline.screen({"frame_id": "test"})
    assert result.state == "HUMAN_REVIEW"
    assert result.requires_human_review
