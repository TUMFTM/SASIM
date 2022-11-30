from dataclasses import dataclass
from typing import List

from model.entities.costs.Costs import Costs
from model.entities.location.Location import Location
from model.entities.segment.Segment import Segment
from model.enums.mode.PublicTransportMode import PublicTransportMode
from model.enums.tarif_zone.TarifZone import TarifZone


@dataclass
class PublicTransportSegment(Segment):
    mode: PublicTransportMode
    duration: float
    distance: float
    costs: Costs
    waypoints: List[Location]
    from_tarif_zone: TarifZone
    to_tarif_zone: TarifZone
