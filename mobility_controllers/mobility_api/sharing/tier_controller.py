import requests

from config.api_keys import tierkey
from classes.Location import Location
from engines.geo_functions import get_distance
import time


def get_location_closest_tier_vehicle(start_location: Location) -> Location:

    start = time.time()

    key = tierkey
    url = 'https://platform.tier-services.io/vehicle?lat=' + str(start_location.get_latitude()) + '&lng=' + \
          str(start_location.get_longitude()) + '&radius=30000'
    with requests.get(url, headers={'X-Api-Key': key}) as tier_resp:
        print("TIER response: " + str(tier_resp))
        resp = tier_resp.json()
        # pprint.pprint(resp)



    try:
        data = resp.get('data')
        number = resp.get('meta').get('rowCount')
        point_min = (data[0].get('lat'), data[0].get('lng'))
        dist_min = get_distance((start_location.get_latitude(), start_location.get_longitude()), point_min)
        for i in range(0, number):
            point = (data[i].get('lat'), data[i].get('lng'))
            dist = get_distance((start_location.get_latitude(), start_location.get_longitude()), point)
            if dist < dist_min:
                dist_min = dist
                point_min = point
    except AttributeError:
        point_min = 0
        print('Tier API AttributeError')

    closest_vehicle = Location(latitude=point_min[0], longitude=point_min[1])

    end = time.time()
    print("tier api: " + str(end - start))

    return closest_vehicle

