import pprint
import time
from datetime import datetime
import requests
import json
from typing import List
import polyline
import pandas as pd

from model.enums.mode.TripMode import TripMode
from model.entities.location.Location import Location

from controllers.muenchenapi.MuenchenapiHelper import MuenchenapiHelper

class MuenchenapiController:

    def __init__(self):
        self.muenchenapi_helper = MuenchenapiHelper()

    def get_response(self, start_location: Location, end_location: Location, mode: TripMode,
                     input_time: datetime = None):
        # 1. convert mode
        muenchenapi_mode = self.muenchenapi_helper.get_muenchenapi_mode_from_mode(mode)

        # 2. getresponse
        start = time.time()

        url = 'https://muenchenapis.de/proxies/metarouter/v1/proxy-k.php?originLat=' + str(
            start_location.lat) + '&originLng=' + str(
            start_location.lon) + '&destinationLat=' + str(end_location.lat) + '&destinationLng=' + str(
            end_location.lon) + '&modalities=' + str(muenchenapi_mode.value)

        response = requests.get(url)
        print("Muenchen API response: " + str(response))
        end = time.time()
        print("muenchen api: " + str(end - start))
        response = response.json()

        return response

    def get_distance(self, response: json)-> float:

        distance = response.get('items')[0].get('distanceInMeters')
        return distance

    def get_duration(self, response: json)-> float:

        # get duration in minutes
        duration = response.get('items')[0].get('travelTimeInSeconds')/60
        return duration

    def get_waypoints(self, response: json)-> List[Location]:

        route_polyline = response.get('items')[0].get('legs')[0].get('polyline')
        coordinates = polyline.decode(route_polyline, 5)
        df_coordinates = pd.DataFrame(coordinates)
        df_coordinates = df_coordinates.apply(lambda x: Location(lat=x[0], lon=x[1]), axis=1)
        list_location = df_coordinates.values.tolist()

        return list_location

#
# muenchenapi_controller = MuenchenapiController()
#
# # Ansprengerstr. 22
# lat1 = 48.1663834
# lon1 = 11.5748712
#
# # Sonnenstra. 11
# lat2 = 48.1377949
# lon2 = 11.5657148
#
# # Ottobrunner Str. 61
# lat3 = 48.1089254
# lon3 = 11.6141669
#
# loc1 = Location(lat=lat1, lon=lon1)
# loc2 = Location(lat=lat2, lon=lon2)
# loc3 = Location(lat=lat3, lon = lon3)
#
# response = muenchenapi_controller.get_response(start_location=loc1, end_location=loc3, mode=TripMode.EMMY)
# # pprint.pprint(response)
