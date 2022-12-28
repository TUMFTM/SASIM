import time

import requests

from model.entities.location.Location import Location


class EmmyController:

    def __init__(self):
        pass

    def get_closest_vehicle(self, start_location: Location) -> Location:
        start = time.time()

        lat_start = start_location.lat
        lon_start = start_location.lon

        url = 'https://emmy.frontend.fleetbird.eu/api/prod/v1.06/cars/?lat=' + str(lat_start) + '&lon=' + str(lon_start)
        response = requests.get(url)
        print("EMMY response: " + str(response))
        response = response.json()

        pickup_point = Location(lat=response[0].get('lat'), lon=response[0].get('lon'))

        end = time.time()
        print("emmy api: " + str(end - start))

        return pickup_point


# ## TESTING
#
# # Ansprengerstr. 22
# lat1 = 48.1663834
# lon1 = 11.5748712
#
# loc1 = Location(lat=lat1, lon=lon1)
#
# emmy_controller = EmmyController()
# print(emmy_controller.get_closest_vehicle(loc1))