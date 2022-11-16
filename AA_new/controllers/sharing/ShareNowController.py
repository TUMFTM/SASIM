import gzip
import json
import time
import uuid

import numpy as np
from paho.mqtt import client as mqtt

from AA_new.entities_new.location.Location import Location
from AA_new.helpers.GeoHelper import GeoHelper


class ShareNowController:

    def __init__(self):
        self.geo_helper = GeoHelper()

    def get_closest_vehicle(self, start_location: Location) -> Location:
        start = time.time()
        global result
        result = ""

        def on_connect(client, userdata, flags, rc):
            print("Connected with result code {0}".format(str(rc)))
            client.subscribe(TOPIC)

        def on_message(client, userdata, msg):
            global result
            result = gzip.decompress(msg.payload).decode("utf-8")

        clientId = f'a:{uuid.uuid4()}'

        client = mqtt.Client(clientId)
        client.tls_set()

        HOST = 'driver.eu.share-now.com'
        PORT = 443
        TOPIC = "C2G/S2C/26/VEHICLELIST.GZ"

        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(HOST, PORT)
        client.loop_start()
        time.sleep(0.3)
        client.loop_stop()

        try:
            result = json.loads(result)
        except json.decoder.JSONDecodeError:
            print("keine Verbindung zu ShareNow möglich")

        vehicle_result = result.get('connectedVehicles')

        distances = []

        # TODO: lambda function for distance calculation
        for i in range(len(vehicle_result)):
            vehicle_location = Location(lat=vehicle_result[i].get('geoCoordinate')['latitude'],
                                        lon=vehicle_result[i].get('geoCoordinate')['longitude'])

            distance = self.geo_helper.get_distance(start_location=vehicle_location, end_location=start_location)
            distances.append(distance)


        closest = vehicle_result[np.argmin(distances)]
        closest_vehicle_location = Location(lat=closest['geoCoordinate']['latitude'],
                                            lon=closest['geoCoordinate']['longitude'])

        end = time.time()
        print("share now api: " + str(end - start))

        return closest_vehicle_location


