from dataclasses import dataclass
from typing import List

from model.entities.costs.Costs import Costs
from model.entities.location.Location import Location
from model.entities.segment.Segment import Segment
from model.enums.mode.IndividualMode import IndividualMode


@dataclass
class IndividualSegment(Segment):
    mode: IndividualMode
    duration: float
    distance: float
    costs: Costs
    waypoints: List[Location]
