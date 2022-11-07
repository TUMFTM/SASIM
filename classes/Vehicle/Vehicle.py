from classes.Location import Location
from classes.Enum.PropulsionType import PropulsionType
from classes.Enum.VehicleType import VehicleType


class Vehicle:

    def get_location(self) -> Location:
        pass

    def get_vehicle_type(self) -> VehicleType:
        pass

    def get_propulsion_type(self) -> PropulsionType:
        pass

    def is_sharing(self) -> bool:
        pass
