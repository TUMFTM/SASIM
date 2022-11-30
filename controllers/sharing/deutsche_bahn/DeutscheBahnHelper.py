import json

from model.entities.location.Location import Location


class DeutscheBahnHelper:

    def get_closest_pickuppoint(self, resp: json, start_location: Location) -> Location:
        try:
            callabike = resp
            items = callabike.get('items')
            location_min = Location(lat=callabike.get('items')[0].get('position').get('coordinates')[1],
                                    lon=callabike.get('items')[0].get('position').get('coordinates')[0])
            dst_min = get_distance(start_location.get_string(), location_min.get_string())
            for i in range(1, len(items)):
                location = Location(lat=callabike.get('items')[i].get('position').get('coordinates')[1],
                                    lon=callabike.get('items')[i].get('position').get('coordinates')[0])
                dst = get_distance(start_location.get_string(), location.get_string())
                if dst < dst_min:
                    dst_min = dst
                    location_min = location

        except AttributeError:
            print("Attribute Error")
            return 0

        return location_min

