from dataclasses import dataclass
from typing import List

from AA_new.entities_new.costs.Costs import Costs
from AA_new.entities_new.location.Location import Location
from AA_new.entities_new.segment.Segment import Segment
from AA_new.enums.mobi_score.MobiScore import MobiScore
from AA_new.enums.mode.TripMode import TripMode


@dataclass
class Trip:
    start_location: Location
    end_location: Location
    trip_mode: TripMode
    segments: List[Segment]
    duration: float
    distance: float
    costs: Costs
    mobi_score: MobiScore