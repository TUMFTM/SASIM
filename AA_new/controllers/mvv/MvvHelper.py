from dataclasses import dataclass
from enum import Enum, auto
from typing import List

import pandas as pd

from AA_new.entities_new.location.Location import Location
from AA_new.enums.mode.IndividualMode import IndividualMode
from AA_new.enums.mode.PublicTransportMode import PublicTransportMode
from AA_new.enums.tarif_zone.MvvTarifZone import MvvTarifZone


class MvvSegmentType(Enum):
    INTERCHANGE = auto()
    WALK_THERE = auto()
    WALK_AWAY = auto()
    TRANSPORTATION = auto()
@dataclass
class MvvSegment:
    waypoints: List[Location]
    duration: float
    distance: float
    departure: int
    arrival: int
    from_tarif_zone: MvvTarifZone
    to_tarif_zone: MvvTarifZone
    segment_type: MvvSegmentType
    mode: PublicTransportMode or IndividualMode

@dataclass
class MvvData:
    mvv_trip: List[MvvSegment]
    from_tarf_zone: MvvTarifZone
    to_tarif_zone: MvvTarifZone


class MvvHelper:

    def get_mvv_mode(self, connectionPartType: str) -> PublicTransportMode or IndividualMode:
        if (connectionPartType == 'UBAHN'):
            mode = PublicTransportMode.METRO

        elif (connectionPartType == 'TRAM'):
            mode = PublicTransportMode.TRAM

        elif (connectionPartType == 'BUS'):
            mode = PublicTransportMode.BUS

        elif (connectionPartType == 'SBAHN' or connectionPartType == 'BAHN'):
            mode =PublicTransportMode.REGIONAL_TRAIN

        elif (connectionPartType == 'FOOTWAY'):
            mode = IndividualMode.WALK
        else:
            print("MVG segment Typ " + str(connectionPartType) + " unbekannt")
            mode = None

        return mode

    def get_mvv_path_as_locations(self, path: dict) -> List[Location]:
        df_path = pd.DataFrame(path)
        df_locations = df_path.apply(lambda x: Location(lat=x['latitude'], lon=x['longitude']), axis=1)
        list_locations = df_locations.values.tolist()
        return list_locations

    def get_mvv_tarif_zone(self, mvg_response):
        mvg_tarif_zone = mvg_response[0].get('efaTicketIds')[0]

        return mvg_tarif_zone