from typing import List

from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Costs.external_costs_helper import add_external_costs
from classes.Enum.SharingCompany import SharingCompany
from classes.Enum.TripType import TripType
from classes.Enum.VehicleType import IndividualVehicleType
from classes.Location import Location
from classes.Segment.OtpRoutingSegment import OtpRoutingSegment
from classes.Trip.Trip import Trip
from classes.Vehicle.IndividualVehicle import IndividualVehicle
from classes.Vehicle.SharingVehicle import SharingVehicle
from engines.geo_functions import get_distance as get_direct_distance


# this is a trip with a sharing vehicle

class SharingTrip(Trip):

    # TODO: change input parameter from company_name to vehicle_type or something similar
    def __init__(self, start_location: Location, end_location: Location, company_name: SharingCompany):
        self.__start_location = start_location
        self.__end_location = end_location
        self.__company_name = company_name

        self.__sharing_vehicle = SharingVehicle(self.__start_location, self.__company_name)

        self.__segments = self.__calculate_segments()
        self.__external_costs = self.__calculate_external_costs()
        self.__internal_costs = self.__calculate_internal_costs()

    def __calculate_segments(self) -> List[OtpRoutingSegment]:
        # TODO: change OtpSegmentType from BICYCLE to ... variable depending on Sharing Company

        walking: IndividualVehicle = IndividualVehicle(vehicle_type=IndividualVehicleType.WALK)

        walking_segment: OtpRoutingSegment = OtpRoutingSegment(self.__start_location,
                                                               self.__sharing_vehicle.get_location(),
                                                               walking)

        ride_segment: OtpRoutingSegment = OtpRoutingSegment(self.__sharing_vehicle.get_location(), self.__end_location,
                                                            self.__sharing_vehicle)

        return ([walking_segment, ride_segment])

    def __calculate_external_costs(self):
        external_costs: ExternalCosts = ExternalCosts()
        for i in range(len(self.__segments)):
            i_external_costs = self.__segments[i].get_external_costs()

            external_costs = add_external_costs(
                external_costs=external_costs,
                i_external_costs=i_external_costs
            )

        return external_costs

    def __calculate_internal_costs(self) -> InternalCosts:
        internal_costs: InternalCosts = InternalCosts(value=0)

        # calculate the sum of the internal costs of all segments
        for i in range(len(self.__segments)):
            i_internal_costs = self.__segments[i].get_internal_costs()
            internal_costs.value += i_internal_costs.value

        return internal_costs

    def get_external_costs(self) -> ExternalCosts:
        return self.__external_costs

    def get_segments(self):
        return self.__segments

    def get_duration(self):
        # calculate the sum of the duration of all segments
        return float(sum(list(map(lambda x: x.get_duration(), self.__segments))))

    def get_distance(self):
        # calculate the sum of the distance of all segments
        return float(sum(list(map(lambda x: x.get_distance(), self.__segments))))

    def get_direct_distance(self):
        direct_distance = get_direct_distance(self.__start_location.get_coordinates(),
                                              self.__end_location.get_coordinates()) / 1000
        return direct_distance

    def get_company_name(self):
        return self.__company_name

    def get_internal_costs(self):
        return self.__internal_costs

    def get_sharing_vehicle(self):
        return self.__sharing_vehicle

    def get_trip_type(self):
        return TripType.SHARING
