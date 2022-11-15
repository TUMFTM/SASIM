from dataclasses import dataclass

from AA_new.entities_new.costs.Costs import Costs
from AA_new.entities_new.location.Location import Location
from AA_new.enums.mode.IndividualMode import SharingMode
from Segment import Segment


@dataclass
class SharingSegment(Segment):
    mode: SharingMode
    duration: float
    distance: float
    costs: Costs
    waypoints: List[Location]
