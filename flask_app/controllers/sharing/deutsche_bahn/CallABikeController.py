import json
import time

import requests

from controllers.sharing.deutsche_bahn.DeutscheBahnHelper import DeutscheBahnHelper
from model.entities.location.Location import Location
from config.api_keys import dbkey


class CallABikeController:

    def __init__(self):
        self.deutsche_bahn_helper = DeutscheBahnHelper()

    def get_closest_vehicle(self, start_location: Location)-> Location:
        start = time.time()

        try:
            lat_start = str(start_location.lat)
            lon_start = str(start_location.lon)
            url = 'https://api.deutschebahn.com/flinkster-api-ng/v1/bookingproposals?lat=' + lat_start + '&lon=' + lon_start + \
                  '&radius=30000&limit=100&providernetwork=2&expand=rentalobject'
            # resp = requests.get(url, headers={'Authorization': 'Bearer 33ff3ff722f73791e2a15c458dd4e9a3'})
            with requests.get(url, headers={'Authorization': dbkey}) as respo:
                print("call a bike response: " + str(respo))
                resp = respo.json()

        except ValueError:
            print('DB API error !!! ValueError')
            resp = 0
        except requests.exceptions.ChunkedEncodingError:
            print('DB API error !!! ChunkedEncodingError')
            resp = 0
        except json.decoder.JSONDecodeError:
            print('DB API error !!! JSONDecode')
            resp = 0
        except requests.exceptions.RequestException:
            print('DB API error !!! RequestException')
            resp = 0

        try:
            closest_vehicle_position = self.deutsche_bahn_helper.get_closest_pickuppoint(resp, start_location)

        except IndexError:
            print('CAB IndexError')
            return None
        except AttributeError:
            print('CAB AttrErr')
            return None
        except TypeError:
            print('CAB TypeErr')
            return None

        end = time.time()
        print("cab api: " + str(end - start))

        return closest_vehicle_position

# ## TESTING
#
# # Ansprengerstr. 22
# lat1 = 48.1663834
# lon1 = 11.5748712
# loc1 = Location(lat=lat1, lon=lon1)
#
# controller = CallABikeController()
# cab_controller.get_closest_vehicle(loc1)