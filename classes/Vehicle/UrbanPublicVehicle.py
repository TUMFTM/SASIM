from classes.Location import Location
from classes.Enum.PropulsionType import PropulsionType
from classes.Vehicle.Vehicle import Vehicle
from classes.Enum.VehicleType import UrbanPublicVehicleType


class UrbanPublicVehicle(Vehicle):

    def __init__(self, vehicle_type: UrbanPublicVehicleType, propulsion_type: PropulsionType=None, location: Location = None,
                 ):
        self.__vehicle_type = vehicle_type
        self.__propulsion_type = propulsion_type
        self.__location = location

    def get_vehicle_type(self) -> UrbanPublicVehicleType:
        return self.__vehicle_type

    def get_location(self) -> Location:
        return self.__location

    def get_propulsion_type(self) -> PropulsionType:
        return self.__propulsion_type

    def is_sharing(self) -> bool:
        return False