from dataclasses import dataclass
from typing import List

from AA_new.entities_new.costs.Costs import Costs
from AA_new.entities_new.location.Location import Location
from AA_new.entities_new.segment.Segment import Segment
from AA_new.enums.mode.SharingMode import SharingMode


@dataclass
class SharingSegment(Segment):
    mode: SharingMode
    duration: float
    distance: float
    costs: Costs
    waypoints: List[Location]
