import time

from geopy.geocoders import Nominatim

from model.entities.location.Location import Location


class GeocodingController:

    def get_location(self, address: str) -> Location:
        start = time.time()

        locator = Nominatim(user_agent="gustav")
        geo_location = locator.geocode(address)

        location = Location(lat=geo_location.latitude, lon=geo_location.longitude)

        end = time.time()
        print("geocoder api: " + str(end - start))

        return location
