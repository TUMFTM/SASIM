from typing import List

from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Costs.external_costs_helper import add_external_costs
from classes.Enum.TripType import TripType
from classes.Enum.VehicleType import UrbanPublicVehicleType
from classes.Location import Location
from classes.Segment.MvgSegment import MvgSegment
from classes.Trip.Trip import Trip
from classes.Vehicle.UrbanPublicVehicle import UrbanPublicVehicle
from engines.geo_functions import get_distance as get_direct_distance
from mobility_controllers.costs.internal_costs_helper import calculate_internal_costs
from mobility_controllers.mobility_api.public_transport.mvg_controller import get_mvg_segments, get_mvv_tarif_zone, \
    get_mvg_response


class PublicTransportTrip(Trip):

    def __init__(self, start_location: Location, end_location: Location):
        self.__start_location = start_location
        self.__end_location = end_location

        # self.__response = get_mvg_response(start_location=self.__start_location, end_location=self.__end_location)
        self.__response = get_mvg_response(start_location=self.__start_location, end_location=self.__end_location)

        self.__trip_calculation = self.__calculate_trip(self.__response)
        self.__segments = self.__trip_calculation[0]

        self.__internal_costs = self.__trip_calculation[1]
        self.__external_costs = self.__trip_calculation[2]

    def __calculate_segments(self, ) -> List[MvgSegment]:
        segments = get_mvg_segments(self.__response)

        return segments

    def __calculate_trip(self, response) -> (List[MvgSegment], ExternalCosts, InternalCosts):
        segments = get_mvg_segments(response)

        external_costs: ExternalCosts = ExternalCosts()
        for i in range(len(segments)):
            i_external_costs = segments[i].get_external_costs()

            external_costs = add_external_costs(
                external_costs=external_costs,
                i_external_costs=i_external_costs
            )

        vehicle = UrbanPublicVehicle(vehicle_type=UrbanPublicVehicleType.PT)
        tarif_zone = get_mvv_tarif_zone(response)

        internal_costs = InternalCosts(value=calculate_internal_costs(vehicle=vehicle, tarif_zone=tarif_zone))

        tarif_zone = get_mvv_tarif_zone(response)

        return segments, internal_costs, external_costs, tarif_zone

    def __calculate_external_costs(self):
        external_costs: ExternalCosts = ExternalCosts()
        for i in range(len(self.__segments)):
            i_external_costs = self.__segments[i].get_external_costs()

            external_costs = add_external_costs(
                external_costs=external_costs,
                i_external_costs=i_external_costs
            )

        return external_costs

    def __calculate_internal_costs(self):
        # TODO: hier irgendwas mit get_tarif_zone ...
        vehicle = UrbanPublicVehicle(vehicle_type=UrbanPublicVehicleType.PT)
        tarif_zone = get_mvv_tarif_zone(self.__response)

        internal_costs = InternalCosts(value=calculate_internal_costs(vehicle=vehicle, tarif_zone=tarif_zone))

        return internal_costs

    def get_segments(self):
        return self.__segments

    def get_duration(self) -> float:
        # calculate the sum of the duration of all segments
        return float(sum(list(map(lambda x: x.get_duration(), self.__segments))))

    def get_distance(self) -> float:
        # calculate the sum of the distance of all segments
        return float(sum(list(map(lambda x: x.get_distance(), self.__segments))))

    def get_direct_distance(self):
        direct_distance = get_direct_distance(self.__start_location.get_coordinates(),
                                              self.__end_location.get_coordinates()) / 1000
        return direct_distance

    def get_external_costs(self) -> ExternalCosts:
        return self.__external_costs

    def get_internal_costs(self) -> InternalCosts:
        return self.__internal_costs

    def get_trip_type(self):
        return TripType.MVG

    def get_tarif_zone(self):
        return get_mvv_tarif_zone(self.__response)
