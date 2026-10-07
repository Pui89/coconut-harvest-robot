from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class HarvestDecision(str,Enum):
    HARVEST="HARVEST"; LOW_CONFIDENCE="LOW_CONFIDENCE"; TARGET_OCCLUDED="TARGET_OCCLUDED"; NOT_REACHABLE="NOT_REACHABLE"; COLLISION_RISK="COLLISION_RISK"; SENSOR_FAILURE="SENSOR_FAILURE"; HUMAN_REVIEW="HUMAN_REVIEW"; UNKNOWN="UNKNOWN"

@dataclass(frozen=True)
class HarvestEvidence:
    perception_confidence:float
    localization_confidence:float
    ripeness_confidence:float
    reachability:float
    collision_clearance_m:float
    sensor_quality:float=1.0
    occlusion:float=0.0
    tracking_stability:float=1.0

@dataclass(frozen=True)
class HarvestabilityResult:
    score:float
    decision:HarvestDecision
    reasons:tuple[str,...]

def score_harvestability(e:HarvestEvidence,min_clearance_m:float=0.20)->HarvestabilityResult:
    vals=[max(0.0,min(1.0,x)) for x in (e.perception_confidence,e.localization_confidence,e.ripeness_confidence,e.reachability,e.sensor_quality,e.tracking_stability)]
    score=sum(vals)/len(vals)*(1.0-max(0.0,min(1.0,e.occlusion)))
    if e.sensor_quality<0.4:return HarvestabilityResult(score,HarvestDecision.SENSOR_FAILURE,("sensor quality below execution threshold",))
    if e.occlusion>0.75:return HarvestabilityResult(score,HarvestDecision.TARGET_OCCLUDED,("target is substantially occluded",))
    if e.collision_clearance_m<min_clearance_m:return HarvestabilityResult(score,HarvestDecision.COLLISION_RISK,("clearance below safety margin",))
    if e.reachability<0.5:return HarvestabilityResult(score,HarvestDecision.NOT_REACHABLE,("target is not sufficiently reachable",))
    if score<0.60:return HarvestabilityResult(score,HarvestDecision.LOW_CONFIDENCE,("evidence below execution threshold",))
    if score<0.80:return HarvestabilityResult(score,HarvestDecision.HUMAN_REVIEW,("candidate requires human review",))
    return HarvestabilityResult(score,HarvestDecision.HARVEST,())
