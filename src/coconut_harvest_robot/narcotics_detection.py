"""Defensive multimodal narcotics-screening adapter. Produces evidence-oriented screening results for human review and never commands actuators."""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

SUPPORTED_CLASSES = ("amphetamine", "heroin", "methamphetamine_crystal", "narcotic_unknown", "unknown_substance")

@dataclass
class SubstanceCandidate:
    label: str
    confidence: float
    bbox: Optional[List[float]] = None
    evidence: List[str] = field(default_factory=list)

@dataclass
class ScreeningResult:
    state: str
    candidates: List[SubstanceCandidate]
    rationale: str
    requires_human_review: bool = True

class NarcoticsScreeningPipeline:
    """Model-agnostic adapter for YOLO/SAM3 + multimodal reasoning."""
    def __init__(self, detector: Optional[Callable[[Dict[str, Any]], List[Dict[str, Any]]]] = None, reasoner: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None, confidence_threshold: float = 0.60):
        self.detector = detector
        self.reasoner = reasoner
        self.confidence_threshold = confidence_threshold

    def screen(self, observation: Dict[str, Any]) -> ScreeningResult:
        detections = self.detector(observation) if self.detector else []
        candidates = []
        for item in detections:
            label = str(item.get("label", "unknown_substance"))
            confidence = float(item.get("confidence", 0.0))
            if label not in SUPPORTED_CLASSES:
                label = "unknown_substance"
            if confidence >= self.confidence_threshold:
                candidates.append(SubstanceCandidate(label, confidence, item.get("bbox"), list(item.get("evidence", []))))
        reasoning = self.reasoner({"observation": observation, "candidates": [c.__dict__ for c in candidates]}) if self.reasoner else {}
        if not candidates:
            return ScreeningResult("UNKNOWN", [], "No sufficiently confident substance candidate; absence of a detection is not proof of absence.")
        state = str(reasoning.get("state", "HUMAN_REVIEW"))
        if state not in {"SUSPECTED_SUBSTANCE", "HUMAN_REVIEW", "UNKNOWN"}:
            state = "HUMAN_REVIEW"
        return ScreeningResult(state, candidates, str(reasoning.get("rationale", "Candidate evidence requires independent human verification.")), True)
