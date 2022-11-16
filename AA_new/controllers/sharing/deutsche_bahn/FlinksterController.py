import time

import requests

from AA_new.controllers.sharing.deutsche_bahn.DeutscheBahnHelper import DeutscheBahnHelper
from AA_new.entities_new.location.Location import Location
from config.api_keys import dbkey


class FlinksterController:

    def __init__(self):
        self.deutsche_bahn_helper = DeutscheBahnHelper()

    def get_closest_vehicle(self, start_location: Location) -> Location:
        start = time.time()
        try:
            lat_start = str(start_location.lat)
            lon_start = str(start_location.lon)
            url = 'https://api.deutschebahn.com/flinkster-api-ng/v1/bookingproposals?lat=' + lat_start + '&lon=' + lon_start + \
                  '&radius=30000&limit=100&providernetwork=1&expand=rentalobject'
            # resp = requests.get(url, headers={'Authorization': 'Bearer 33ff3ff722f73791e2a15c458dd4e9a3'})
            with requests.get(url, headers={'Authorization': dbkey}) as respo:
                print("DB response: " + str(respo))
                resp = respo.json()

        except ValueError:
            print('DB API error !!! ValueError')
            resp = 0
        except requests.exceptions.ChunkedEncodingError:
            print('DB API error !!! ChunkedEncodingError')
            resp = 0
        except json_functions.decoder.JSONDecodeError:
            print('DB API error !!! JSONDecode')
            resp = 0
        except requests.exceptions.RequestException:
            print('DB API error !!! RequestException')
            resp = 0

        try:
            closest_vehicle_position = self.deutsche_bahn_helper.get_closest_pickuppoint(resp, start_location)

        except IndexError:
            print('Flinkster IndexError')
            return None
        except AttributeError:
            print('Flinkster AttrErr')
            return None
        except TypeError:
            print('Flinkster TypeErr')
            return None

        end = time.time()
        print("flinkster api: " + str(end - start))

        return closest_vehicle_position

#