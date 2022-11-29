from dataclasses import dataclass
from typing import List

from AA_new.model.entities.costs.Costs import Costs
from AA_new.model.entities.location.Location import Location
from AA_new.model.entities.segment.Segment import Segment
from AA_new.model.enums.mode.PublicTransportMode import PublicTransportMode
from AA_new.model.enums.tarif_zone.TarifZone import TarifZone


@dataclass
class PublicTransportSegment(Segment):
    mode: PublicTransportMode
    duration: float
    distance: float
    costs: Costs
    waypoints: List[Location]
    from_tarif_zone: TarifZone
    to_tarif_zone: TarifZone
