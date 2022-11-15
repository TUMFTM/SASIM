import time

import requests

from AA_new.entities_new.location.Location import Location
from AA_new.helpers.GeoHelper import GeoHelper
from config.api_keys import tierkey


class TierController:

    def __init__(self):
        self.geo_helper = GeoHelper()

    def get_closest_vehicle(self, start_location: Location) -> Location:
        start = time.time()

        key = tierkey
        url = 'https://platform.tier-services.io/vehicle?lat=' + str(start_location.lat) + '&lng=' + \
              str(start_location.lon) + '&radius=30000'
        with requests.get(url, headers={'X-Api-Key': key}) as tier_resp:
            print("TIER response: " + str(tier_resp))
            resp = tier_resp.json()
            # pprint.pprint(resp)

        try:
            data = resp.get('data')
            number = resp.get('meta').get('rowCount')
            point_min = (data[0].get('lat'), data[0].get('lng'))
            dist_min = self.geo_helper.get_distance((start_location.lat, start_location.lon), point_min)
            for i in range(0, number):
                point = (data[i].get('lat'), data[i].get('lng'))
                dist = self.geo_helper.get_distance((start_location.lat, start_location.lon), point)
                if dist < dist_min:
                    dist_min = dist
                    point_min = point
        except AttributeError:
            point_min = 0
            print('Tier API AttributeError')

        closest_vehicle = Location(lat=point_min[0], lon=point_min[1])

        end = time.time()
        print("tier api: " + str(end - start))

        return closest_vehicle

# ## TESTING
#
# # Ansprengerstr. 22
# lat1 = 48.1663834
# lon1 = 11.5748712
#
# loc1 = Location(lat=lat1, lon=lon1)
#
# controller = TierController()
# print(controller.get_closest_vehicle(loc1))