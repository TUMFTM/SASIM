from engines.geocoder import get_location

class Location:

    def __init__(self, latitude: float = 0.0, longitude: float = 0.0, address: str = ""):
        self.latitude = latitude
        self.longitude = longitude
        self.address = address

        self.__set_parameters(self.latitude, self.longitude, self.address)

    def get_coordinates(self) -> (float, float):
        return(self.latitude, self.longitude)

    def get_longitude(self) -> float:
        return self.longitude

    def get_latitude(self) -> float:
        return self.latitude

    def get_dict(self) -> dict:
        return {
            'lat': self.latitude,
            'lon': self.longitude
        }

    def get_string(self) -> str:
        return (str(self.latitude) + ", " + str(self.longitude))

    def get_address(self) -> str:
        return self.address

    def __set_parameters(self, latitude, longitude, address):

        if (latitude == 0.0 and longitude == 0.0 and address != ""):
            location = get_location(address)

            if (location != None):
                self.latitude = location.latitude
                self.longitude = location.longitude

            else:
                print("\nAdresse wurde nicht gfunden. \nGeben sie die latitude und longitude Werte an oder eine korrekte Adresse")

        if (latitude == 0.0 and longitude == 0.0 and address == ""):
            print("\nLocation objekte müssen entweder latitude und longitude oder addresse enthalten")
            return 0

