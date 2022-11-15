from typing import List

import geopy.distance
import pandas as pd

from AA_new.entities_new.location.Location import Location


class GeoHelper:

    def get_distance(self, start_coords, end_coords):
        return int(geopy.distance.distance(start_coords, end_coords).m)


    def calculate_total_distance_from_location_list(self, list_location: List[Location]):

        length = len(list_location)

        array1 = list_location[0:length-1]
        array2 = list_location[1:length]


        df_1= pd.DataFrame(array1, columns=['array1'])
        df_1['array2'] = pd.DataFrame(array2)
        df_1['distance'] = df_1.apply(lambda x: get_distance((x.array1.lat, x.array1.lon), (x.array2.lat, x.array2.lon)), axis=1)

        distance = df_1['distance'].sum()
        return float(distance)
