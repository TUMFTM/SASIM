import json
import time as t
from datetime import datetime
from typing import List

import pandas as pd
import polyline
import requests
from controllers.otp.OtpHelper import OtpHelper
from model.entities.location.Location import Location
from model.enums.mode.TripMode import TripMode


class OtpController:

    def __init__(self):

        self.otp_helper = OtpHelper()

    def get_waypoints(self, response: json) -> List[Location] or None:
        try:

            list_locations = []
            legs = response["plan"].get('itineraries')[0].get('legs')
            for i in range(len(legs)):
                # TODO: optionally generate different segments from one otp segment
                result = legs[i].get('legGeometry').get('points')
                coordinates = polyline.decode(result, 5)
                df_coordinates = pd.DataFrame(coordinates)
                df_coordinates = df_coordinates.apply(lambda x: Location(x[0], x[1]), axis=1)
                list_locations.extend(df_coordinates.values.tolist())

            return (list_locations)

        except KeyError:
            print('OTP KeyError route coordinates')
            return None

        except IndexError:
            print("Liste der OTP Strecken ist leer")
            return None


    def get_distance(self, response: json) -> float:
        try:
            itineraries = (response["plan"].get("itineraries"))
            it = itineraries[0]
            legs = it['legs']
            dist = 0
            for leg in legs:
                dist += int(leg['distance'])
        except KeyError:
            print('OTP KeyError distance')
            return 0
        except IndexError:
            print("Liste der OTP Strecken ist leer")
            return 0

        return int(dist)


    def get_duration(self, response: json) -> float:
        try:
            itineraries = (response["plan"].get("itineraries"))
            duration = 0
            for nr in range(0, len(itineraries)):
                duration += (itineraries[nr].get("duration"))

        except IndexError:
            print("Liste der OTP Strecken ist leer")
            return 0

        except KeyError:
            print('OTP KeyError duration')
            return 0

        return duration / 60

    def get_response(self, start_location: Location, end_location: Location, mode: TripMode,
                     input_time=None, input_waxWalkDistance='500'):

        mode = self.otp_helper.mode_to_otp_mode(mode).value
        start_location = self.otp_helper.location_to_otp_format(start_location)
        end_location = self.otp_helper.location_to_otp_format(end_location)

        if not input_time:
            input_time = datetime.now()

            # input_time = '1:02pm&date=22-02-2020'
        start = t.time()
        response = requests.get(
            "http://localhost:8080/otp/routers/default/plan?fromPlace=" + start_location + "&toPlace=" +
            end_location + "&time=" + str(input_time.hour) + ":" + str(input_time.minute) + "&date=" +
            str(input_time.month) + "-" + str(input_time.day) + "-" + str(input_time.year) + "&mode=" +
            mode + "&maxWalkDistance=50000&arriveBy=false")
        print("otp response: " + str(response))

        resp = json.loads(response.content)

        if 'error' in resp:
            print("Error in otp request")

        if (resp["plan"].get("itineraries") == []):
            print("Keine OTP Strecke für diesen Start- und End-Standort und den Modus " + str(
                mode) + " gefunden.\nVersuchen Sie es nochmal")

        end = t.time()
        print("otp request: " + str(end - start))

        return resp

