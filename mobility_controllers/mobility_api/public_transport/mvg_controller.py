import time
from datetime import datetime
from typing import List

import mvg_api
import pandas as pd

from classes.Enum.SegmentType import MvgSegmentType
from classes.Enum.VehicleType import IndividualVehicleType, UrbanPublicVehicleType
from classes.Location import Location
from classes.Segment.MvgSegment import MvgSegment
from classes.Vehicle.IndividualVehicle import IndividualVehicle
from classes.Vehicle.UrbanPublicVehicle import UrbanPublicVehicle
from engines.geo_functions import calculate_total_distance_from_location_list


def get_mvg_response(start_location: Location, end_location: Location, input_time: datetime = None):
    start = time.time()
    try:
        if not input_time:
            input_time = datetime.now()
        response = mvg_api.get_route((start_location.get_latitude(), start_location.get_longitude()),
                                     (end_location.get_latitude(), end_location.get_longitude()), time=input_time,
                                     arrival_time=False, max_walk_time_to_start=None, max_walk_time_to_dest=None,
                                     change_limit=None)

    except TypeError:
        print('MVG API error')
        response = None

    end = time.time()
    print("mvg request: " + str(end - start))

    return response


def get_mvg_segments(response) -> List[MvgSegment]:
    trip = response[0].get('connectionPartList')

    # loop over whole set of response
    return create_mvg_segments(trip)


# this function is not used, but can be useful, if the selection between multiple PT trips should be implemented

def get_multiple_mvg_trips(start_location: Location, end_location: Location, input_time: datetime = None):
    response = get_mvg_response(start_location, end_location)

    trips = []
    for i in range(len(response)):
        trip = create_mvg_segments(response[i].get('connectionPartList'))
        segment_types = list(map(lambda x: x.get_pt_segment_type(), trip))
        duration = float(sum(list(map(lambda x: x.get_duration(), trip))))
        trips.append((trip, segment_types, duration))

    return trips


def create_mvg_segments(mvg_trip):
    result = []
    segments: List[MvgSegment] = []

    # loop over whole set of trip
    for i in range(len(mvg_trip)):

        duration = (mvg_trip[i].get('arrival') - mvg_trip[i].get('departure')) / (1000 * 60)

        if (mvg_trip[i].get('connectionPartType') == 'TRANSPORTATION'):
            vehicle = get_mvg_vehicle(mvg_trip[i].get('product'))
            mvg_segment_type = MvgSegmentType.TRANSPORTATION
            from_zone = mvg_trip[i].get('from').get('tariffZones')
            to_zone = mvg_trip[i].get('to').get('tariffZones')

        else:
            vehicle = get_mvg_vehicle(mvg_trip[i].get('connectionPartType'))
            if (i == 0):
                mvg_segment_type = MvgSegmentType.WALK_THERE
            else:
                mvg_segment_type = MvgSegmentType.WALK_AWAY
            from_zone = 'walk'
            to_zone = 'walk'

        path = mvg_trip[i].get('path')
        path_locations = get_mvg_path_as_locations(path)
        distance = calculate_total_distance_from_location_list(path_locations) / 1000
        departure = mvg_trip[i].get('departure')
        arrival = mvg_trip[i].get('arrival')

        result_element = {
            'type': type,
            'path': path_locations,
            'duration': duration,
            'segment_type': mvg_segment_type
        }

        result.append(result_element)
        segments.append(
            MvgSegment(duration=duration, distance=distance, waypoints=path_locations, vehicle=vehicle,
                       departure=departure, arrival=arrival, pt_segment_type=mvg_segment_type, from_zone=from_zone,
                       to_zone=to_zone))

        # interchangePath is part of a connectionPart, but needs to generate a seperate WALK segment
        if (mvg_trip[i].get('interchangePath') != []):
            interchange_vehicle = IndividualVehicle(vehicle_type=IndividualVehicleType.WALK)
            mvg_segment_type = MvgSegmentType.INTERCHANGE
            duration = 0
            interchange_path = mvg_trip[i].get('interchangePath')
            interchange_path_locations = get_mvg_path_as_locations(interchange_path)
            distance = calculate_total_distance_from_location_list(interchange_path_locations) / 1000
            departure = mvg_trip[i].get('departure')
            arrival = mvg_trip[i].get('arrival')
            from_zone = 'walk'
            to_zone = 'walk'

            segments.append(MvgSegment(duration=duration, distance=distance, waypoints=interchange_path_locations,
                                       vehicle=interchange_vehicle, departure=departure, arrival=arrival,
                                       pt_segment_type=mvg_segment_type, from_zone=from_zone, to_zone=to_zone))

    return segments


def get_mvg_vehicle(connectionPartType: str) -> UrbanPublicVehicle or IndividualVehicle:
    if (connectionPartType == 'UBAHN'):
        vehicle = UrbanPublicVehicle(vehicle_type=UrbanPublicVehicleType.UBAHN)

    elif (connectionPartType == 'TRAM'):
        vehicle = UrbanPublicVehicle(vehicle_type=UrbanPublicVehicleType.TRAM)

    elif (connectionPartType == 'BUS'):
        vehicle = UrbanPublicVehicle(vehicle_type=UrbanPublicVehicleType.BUS)

    elif (connectionPartType == 'SBAHN' or connectionPartType == 'BAHN'):
        vehicle = UrbanPublicVehicle(vehicle_type=UrbanPublicVehicleType.SBAHN)

    elif (connectionPartType == 'FOOTWAY'):
        vehicle = IndividualVehicle(vehicle_type=IndividualVehicleType.WALK)

    else:
        print("MVG segment Typ " + str(connectionPartType) + " unbekannt")
        vehicle = None

    return vehicle


# convert mvg waypoints in a list of locations: List[location]
def get_mvg_path_as_locations(path: dict) -> List[Location]:
    df_path = pd.DataFrame(path)
    df_locations = df_path.apply(lambda x: Location(latitude=x['latitude'], longitude=x['longitude']), axis=1)
    list_locations = df_locations.values.tolist()
    return list_locations


def get_mvv_tarif_zone(mvg_response):
    mvg_tarif_zone = mvg_response[0].get('efaTicketIds')[0]

    return mvg_tarif_zone
