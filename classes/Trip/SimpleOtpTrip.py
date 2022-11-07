from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Enum.TripType import TripType
from classes.Location import Location
from classes.Segment.OtpRoutingSegment import OtpRoutingSegment
from classes.Trip.Trip import Trip
from classes.Vehicle.Vehicle import Vehicle
from engines.geo_functions import get_distance as get_direct_distance


class SimpleOtpTrip(Trip):

    def __init__(self, start_location: Location, end_location: Location, vehicle: Vehicle):
        self.__start_location = start_location
        self.__end_location = end_location
        self.__vehicle = vehicle

        self.__segment = self.__fetch_segment()
        self.__external_costs: ExternalCosts = self.__calculate_external_costs()
        self.__internal_costs: InternalCosts = self.__calculate_internal_costs()

    def __fetch_segment(self) -> OtpRoutingSegment:
        segment = OtpRoutingSegment(self.__start_location, self.__end_location, self.__vehicle)
        return segment

    def get_segments(self) -> OtpRoutingSegment:
        return self.__segment

    def get_duration(self) -> float:
        return (self.__segment.get_duration())

    def get_distance(self):
        return (self.__segment.get_distance())

    def get_direct_distance(self):
        direct_distance = get_direct_distance(self.__start_location.get_coordinates(),
                                              self.__end_location.get_coordinates()) / 1000
        return direct_distance

    def __calculate_external_costs(self) -> ExternalCosts:
        external_costs = self.__segment.get_external_costs()
        return external_costs

    def __calculate_internal_costs(self) -> InternalCosts:
        internal_costs = self.__segment.get_internal_costs()
        return internal_costs

    def get_external_costs(self) -> ExternalCosts:
        return self.__external_costs

    def get_internal_costs(self) -> InternalCosts:
        return self.__internal_costs

    def get_trip_type(self):
        return TripType.SIMPLE
