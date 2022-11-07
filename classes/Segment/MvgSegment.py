from typing import List

from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Enum.SegmentType import MvgSegmentType
from classes.Enum.TarifZoneMVV import TarifZoneMVV
from classes.Location import Location
from classes.Segment.Segment import AbstractSegment
from classes.Vehicle.Vehicle import Vehicle
from mobility_controllers.costs.external_costs_per_km_helper import calculate_external_costs


class MvgSegment(AbstractSegment):

    def __init__(self, duration: float, distance: float, waypoints: List[Location], vehicle: Vehicle, from_zone,
                 to_zone, departure=None, arrival=None, pt_segment_type=None):
        self.__duration: float = duration
        self.__waypoints: List[Location] = waypoints
        self.__vehicle: Vehicle = vehicle
        self.__distance: float = distance
        self.__from_zone: TarifZoneMVV = from_zone
        self.__to_zone: TarifZoneMVV = to_zone
        self.__pt_segment_type = pt_segment_type
        self.__external_costs: ExternalCosts = self.__calculate_external_costs()

    def __calculate_external_costs(self) -> ExternalCosts:
        external_costs = calculate_external_costs(distance=self.__distance, vehicle=self.__vehicle)
        return external_costs

    def get_waypoints(self) -> List[Location]:
        return self.__waypoints

    def get_distance(self) -> float:
        return self.__distance

    def get_duration(self) -> float:
        return self.__duration

    def get_vehicle(self) -> Vehicle:
        return self.__vehicle

    def get_external_costs(self) -> ExternalCosts:
        return self.__external_costs

    def get_from_zone(self)-> TarifZoneMVV:
        return self.__from_zone

    def get_to_zone(self)-> TarifZoneMVV:
        return self.__to_zone

    def get_internal_costs(self) -> InternalCosts:
        return InternalCosts(value=0)

    def get_pt_segment_type(self) -> MvgSegmentType:
        return self.__pt_segment_type
