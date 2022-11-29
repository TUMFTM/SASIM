from typing import List

import geopy.distance
import pandas as pd

from AA_new.model.entities.location.Location import Location


class GeoHelper:

    def get_distance(self, start_location: Location, end_location: Location):

        start_coords = (start_location.lat, start_location.lon)
        end_coords = (end_location.lat, end_location.lon)

        return int(geopy.distance.distance(start_coords, end_coords).m)

    def calculate_total_distance_from_location_list(self, list_location: List[Location]):
        length = len(list_location)

        array1 = list_location[0:length - 1]
        array2 = list_location[1:length]

        df_1 = pd.DataFrame(array1)
        df_1 = df_1.rename(columns={'lat': 'lat_1', 'lon': 'lon_1'})

        df_2 = pd.DataFrame(array2)
        df_2 = df_2.rename(columns={'lat': 'lat_2', 'lon': 'lon_2'})
        df = pd.concat([df_1, df_2], axis=1)

        df['distance'] = df.apply(
            lambda x: self.get_distance(Location(x.lat_1, x.lon_1), Location(x.lat_2, x.lon_2)), axis=1)

        distance = df['distance'].sum()
        return float(distance)
