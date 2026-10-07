from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class SafetyDecision(str,Enum):
    APPROVE="APPROVE"; BLOCK="BLOCK"

@dataclass(frozen=True)
class SafetyLimits:
    min_clearance_m:float=0.20
    max_speed_mps:float=0.50
    max_force_n:float=500.0
    max_workspace_height_m:float=14.0

@dataclass(frozen=True)
class ActionCandidate:
    target_id:str
    confidence:float
    clearance_m:float
    speed_mps:float
    force_n:float
    height_m:float
    emergency_stop:bool=False
    human_in_exclusion_zone:bool=False
    collision_free:bool=True

@dataclass(frozen=True)
class SafetyResult:
    decision:SafetyDecision
    reasons:tuple[str,...]

def validate_action(a:ActionCandidate,limits:SafetyLimits=SafetyLimits())->SafetyResult:
    r=[]
    if a.emergency_stop:r.append("emergency stop active")
    if a.human_in_exclusion_zone:r.append("human detected in exclusion zone")
    if not a.collision_free:r.append("collision check failed")
    if a.confidence<0.80:r.append("confidence below execution threshold")
    if a.clearance_m<limits.min_clearance_m:r.append("workspace clearance too small")
    if a.speed_mps>limits.max_speed_mps:r.append("speed exceeds limit")
    if a.force_n>limits.max_force_n:r.append("force exceeds limit")
    if a.height_m>limits.max_workspace_height_m:r.append("workspace height exceeds limit")
    return SafetyResult(SafetyDecision.BLOCK if r else SafetyDecision.APPROVE,tuple(r))
