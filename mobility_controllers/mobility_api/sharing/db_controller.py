import json
import time

import requests

from config.api_keys import dbkey
from classes.Location import Location
from engines.geo_functions import get_distance


def get_location_closest_cab_vehicle(start_location: Location) -> Location or None:
    start = time.time()

    try:
        lat_start = str(start_location.get_latitude())
        lon_start = str(start_location.get_longitude())
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
        closest_vehicle_position = get_closest_pickuppoint(resp, start_location)

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


def get_location_closest_flinkster_vehicle(start_location: Location) -> Location or None:
    start = time.time()
    try:
        lat_start = str(start_location.get_latitude())
        lon_start = str(start_location.get_longitude())
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
        closest_vehicle_position = get_closest_pickuppoint(resp, start_location)

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


def get_closest_pickuppoint(resp: json, start_location: Location)-> Location:
    try:
        callabike = resp
        items = callabike.get('items')
        location_min = Location(latitude=callabike.get('items')[0].get('position').get('coordinates')[1],
                                longitude=callabike.get('items')[0].get('position').get('coordinates')[0])
        dst_min = get_distance(start_location.get_string(), location_min.get_string())
        for i in range(1, len(items)):
            location = Location(latitude=callabike.get('items')[i].get('position').get('coordinates')[1],
                                longitude=callabike.get('items')[i].get('position').get('coordinates')[0])
            dst = get_distance(start_location.get_string(), location.get_string())
            if dst < dst_min:
                dst_min = dst
                location_min = location

    except AttributeError:
        print("Attribute Error")
        return 0

    return location_min
