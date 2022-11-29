from dataclasses import dataclass
from typing import List

from AA_new.model.entities.costs.Costs import Costs
from AA_new.model.entities.location.Location import Location
from AA_new.model.entities.segment.Segment import Segment
from AA_new.model.enums.mode.SharingMode import SharingMode


@dataclass
class SharingSegment(Segment):
    mode: SharingMode
    duration: float
    distance: float
    costs: Costs
    waypoints: List[Location]
