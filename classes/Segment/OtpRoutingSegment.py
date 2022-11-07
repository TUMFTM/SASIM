from typing import List

from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Enum.SegmentType import OtpSegmentType
from classes.Enum.VehicleType import IndividualVehicleType
from classes.Location import Location
from classes.Segment.Segment import AbstractRoutingSegment
from classes.Vehicle.IndividualVehicle import IndividualVehicle
from classes.Vehicle.SharingVehicle import SharingVehicle
from classes.Vehicle.Vehicle import Vehicle
from mobility_controllers.costs.external_costs_per_km_helper import calculate_external_costs
from mobility_controllers.costs.internal_costs_helper import calculate_internal_costs
from mobility_controllers.open_trip_planner.open_trip_planner import otp_get_response, otp_get_distance, otp_get_duration, otp_get_route_coordinates
from mobility_controllers.open_trip_planner.otp_helper import vehicle_to_otp_type


class OtpRoutingSegment(AbstractRoutingSegment):

    def __init__(self, start_loaction: Location, end_location: Location, vehicle: IndividualVehicle or SharingVehicle):
        self.__start_location = start_loaction
        self.__end_location = end_location
        self.__vehicle = vehicle

        self.__response = self.__receive_response(self.__start_location, self.__end_location,
                                                  self.__vehicle.get_vehicle_type())

        self.__distance = self.__calculate_distance()
        self.__duration = self.__calculate_duration()
        self.__waypoints = self.__calculate_waypoints()
        self.__external_costs = self.__calculate_external_costs()
        self.__internal_costs = self.__calculate_internal_costs()

    def __receive_response(self, start_location: Location, end_location: Location,
                           vehicle_type: IndividualVehicleType) -> dict:
        otp_segment_type = self.__get_otp_segment_type(vehicle_type)

        return otp_get_response(start_location, end_location,
                                otp_segment_type)

    def get_distance(self) -> float:
        return self.__distance

    def get_duration(self) -> float:
        return self.__duration

    def get_waypoints(self) -> List[Location]:
        return self.__waypoints

    def get_vehicle(self) -> Vehicle:
        return self.__vehicle

    def get_external_costs(self) -> ExternalCosts:
        return self.__external_costs

    def get_internal_costs(self) -> InternalCosts:
        return self.__internal_costs

    def __get_otp_segment_type(self, vehicle_type: IndividualVehicleType) -> OtpSegmentType:
        return vehicle_to_otp_type(vehicle_type)

    def __calculate_distance(self) -> float:
        return float(otp_get_distance(self.__response) / 1000)

    def __calculate_duration(self) -> float:
        return float(otp_get_duration(self.__response) / 60)

    def __calculate_waypoints(self):
        return otp_get_route_coordinates(self.__response)

    def __calculate_external_costs(self) -> ExternalCosts:
        external_costs = calculate_external_costs(distance=self.get_distance(), vehicle=self.__vehicle)
        return external_costs

    def __calculate_internal_costs(self) -> InternalCosts:
        internal_costs = InternalCosts(
            value=calculate_internal_costs(vehicle=self.__vehicle, distance=self.__distance, duration=self.__duration))
        return internal_costs
