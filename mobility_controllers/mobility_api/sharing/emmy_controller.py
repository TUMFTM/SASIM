
import requests
import time

from classes.Location import Location
import csv


def get_location_closest_emmy_vehicle(start_location: Location)-> Location:
    start = time.time()


    lat_start = start_location.get_latitude()
    lon_start = start_location.get_longitude()

    url = 'https://emmy.frontend.fleetbird.eu/api/prod/v1.06/cars/?lat=' + str(lat_start) + '&lon=' + str(lon_start)
    response = requests.get(url)
    print("EMMY response: " + str(response))
    response = response.json()

    pickup_point = Location(latitude=response[0].get('lat'), longitude=response[0].get('lon'))

    end = time.time()
    print("emmy api: " + str(end - start))

    return pickup_point