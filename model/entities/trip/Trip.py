from dataclasses import dataclass
from typing import List

from model.entities.costs.Costs import Costs
from model.entities.location.Location import Location
from model.entities.segment.Segment import Segment
from model.enums.mobi_score.MobiScore import MobiScore
from model.enums.mode.TripMode import TripMode


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