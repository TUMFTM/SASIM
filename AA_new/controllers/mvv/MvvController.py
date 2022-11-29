import json
import time
from datetime import datetime
from typing import List

import mvg_api

from AA_new.controllers.mvv.MvvHelper import MvvHelper
from AA_new.controllers.mvv.MvvHelper import MvvSegmentData
from AA_new.controllers.mvv.MvvHelper import MvvSegmentType
from AA_new.controllers.mvv.MvvHelper import MvvTripData
from AA_new.model.entities.location.Location import Location
from AA_new.model.enums.mode.IndividualMode import IndividualMode
from AA_new.model.enums.mode.PublicTransportMode import PublicTransportMode
from AA_new.model.enums.tarif_zone.MvvTarifZone import MvvTarifZone
from AA_new.helpers.GeoHelper import GeoHelper


class MvvController:

    def __init__(self):
        self.mvv_helper = MvvHelper()
        self.geo_helper = GeoHelper()

    def get_mvv_waypoints(self, response) -> List[List[Location]]:
        pass

    def get_mvv_modes(self) -> List[PublicTransportMode]:
        pass

    def get_from_tarif_zone(self) -> MvvTarifZone:
        pass

    def get_to_tarif_zone(self) -> MvvTarifZone:
        pass

    def get_durations(self) -> List[float]:
        pass

    def get_distances(self) -> List[float]:
        pass

    def get_response(self, start_location: Location, end_location: Location, input_time: datetime = None) -> json:
        start = time.time()
        try:
            if not input_time:
                input_time = datetime.now()
            response = mvg_api.get_route((start_location.lat, start_location.lon),
                                         (end_location.lat, end_location.lon), time=input_time,
                                         arrival_time=False, max_walk_time_to_start=None, max_walk_time_to_dest=None,
                                         change_limit=None)

        except TypeError:
            print('MVG API error')
            response = None

        end = time.time()
        print("mvg request: " + str(end - start))

        return response

    def get_mvv_trip_data(self, response) -> MvvTripData:

        global path
        mvv_trip = response[0].get('connectionPartList')

        result = []
        segments: List[MvvSegmentData] = []

        # loop over whole set of trip
        for i in range(len(mvv_trip)):

            duration = (mvv_trip[i].get('arrival') - mvv_trip[i].get('departure')) / (1000 * 60)

            if (mvv_trip[i].get('connectionPartType') == 'TRANSPORTATION'):
                mode = self.mvv_helper.get_mvv_mode(mvv_trip[i].get('product'))
                mvv_segment_type = MvvSegmentType.TRANSPORTATION
                from_zone = mvv_trip[i].get('from').get('tariffZones')
                to_zone = mvv_trip[i].get('to').get('tariffZones')

            else:
                mode = self.mvv_helper.get_mvv_mode(mvv_trip[i].get('connectionPartType'))
                if (i == 0):
                    mvv_segment_type = MvvSegmentType.WALK_THERE
                    from_zone = mvv_trip[i].get('to').get('tariffZones')
                    to_zone = mvv_trip[i].get('to').get('tariffZones')
                else:
                    mvv_segment_type = MvvSegmentType.WALK_AWAY
                    from_zone = mvv_trip[i].get('from').get('tariffZones')
                    to_zone = mvv_trip[i].get('from').get('tariffZones')

            path = mvv_trip[i].get('path')
            path_locations = self.mvv_helper.get_mvv_path_as_locations(path)
            distance = self.geo_helper.calculate_total_distance_from_location_list(path_locations)
            departure = mvv_trip[i].get('departure')
            arrival = mvv_trip[i].get('arrival')

            result_element = {
                'type': type,
                'path': path_locations,
                'duration': duration,
                'segment_type': mvv_segment_type
            }

            result.append(result_element)
            segments.append(
                MvvSegmentData(duration=duration,
                               distance=distance,
                               waypoints=path_locations,
                               mode=mode,
                               segment_type=mvv_segment_type,
                               departure=departure,
                               arrival=arrival,
                               from_tarif_zone=from_zone,
                               to_tarif_zone=to_zone))

            # interchangePath is part of a connectionPart, but needs to generate a seperate WALK segment
            if (mvv_trip[i].get('interchangePath') != []):
                interchange_mode = IndividualMode.WALK
                mvv_segment_type = MvvSegmentType.INTERCHANGE
                duration = 0
                interchange_path = mvv_trip[i].get('interchangePath')
                interchange_path_locations = self.mvv_helper.get_mvv_path_as_locations(interchange_path)
                distance = self.geo_helper.calculate_total_distance_from_location_list(interchange_path_locations)
                departure = mvv_trip[i].get('departure')
                arrival = mvv_trip[i].get('arrival')

                segments.append(MvvSegmentData(duration=duration,
                                               distance=distance,
                                               waypoints=interchange_path_locations,
                                               mode=interchange_mode,
                                               segment_type=mvv_segment_type,
                                               departure=departure,
                                               arrival=arrival,
                                               from_tarif_zone=from_zone,
                                               to_tarif_zone=to_zone))

        trip_from_tarif_zone = segments[0].from_tarif_zone
        trip_to_tarif_zone = segments[0].to_tarif_zone
        mvv_ticket_name = response[0].get('efaTicketIds')[0]

        mvv_data = MvvTripData(mvv_trip=segments, from_tarf_zone=trip_from_tarif_zone, to_tarif_zone=trip_to_tarif_zone,
                               mvv_ticket_name=mvv_ticket_name)

        return mvv_data



