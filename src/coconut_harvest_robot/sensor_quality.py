from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class SensorStatus(str, Enum):
    OK="OK"; DEGRADED="DEGRADED"; MISSING="MISSING"; UNSYNCHRONIZED="UNSYNCHRONIZED"

@dataclass(frozen=True)
class SensorObservation:
    name:str
    available:bool=True
    quality:float=1.0
    timestamp_s:float|None=None
    max_skew_s:float=0.05

@dataclass(frozen=True)
class SensorHealthReport:
    status:SensorStatus
    quality:float
    timestamp_skew_s:float
    reasons:tuple[str,...]

def assess_sensor_health(observations:list[SensorObservation])->SensorHealthReport:
    if not observations: return SensorHealthReport(SensorStatus.MISSING,0.0,float("inf"),("no sensors supplied",))
    active=[x for x in observations if x.available]
    if not active: return SensorHealthReport(SensorStatus.MISSING,0.0,float("inf"),("all sensors unavailable",))
    qs=[max(0.0,min(1.0,x.quality)) for x in active]
    ts=[x.timestamp_s for x in active if x.timestamp_s is not None]
    skew=max(ts)-min(ts) if len(ts)>1 else 0.0
    reasons=[]
    if any(q<0.5 for q in qs): reasons.append("one or more sensors are degraded")
    if len(active)!=len(observations): reasons.append("one or more sensors are missing")
    allowed=min(x.max_skew_s for x in active)
    if skew>allowed: reasons.append("sensor timestamps are not synchronized")
    status=SensorStatus.UNSYNCHRONIZED if skew>allowed else (SensorStatus.DEGRADED if reasons else SensorStatus.OK)
    return SensorHealthReport(status,sum(qs)/len(qs),skew,tuple(reasons))
