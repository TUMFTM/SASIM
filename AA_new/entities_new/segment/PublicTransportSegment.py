from dataclasses import dataclass

from AA_new.entities_new.costs.Costs import Costs
from AA_new.entities_new.location.Location import Location
from AA_new.enums.mode.IndividualMode import PublicTransportMode
from AA_new.enums.tarif_zone.TarifZone import TarifZone
from Segment import Segment


@dataclass
class PublicTransportSegment(Segment):
    mode: PublicTransportMode
    duration: float
    distance: float
    costs: Costs
    waypoints: List[Location]
    from_tarif_zone: TarifZone
    to_tarif_zone: TarifZone
