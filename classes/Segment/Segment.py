from typing import List

from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Enum.SegmentType import AbstractSegmentType
from classes.Location import Location
from classes.Vehicle.Vehicle import Vehicle


class AbstractSegment:

    def get_waypoints(self) -> List[Location]:
        pass

    def get_distance(self) -> float:
        pass

    def get_duration(self) -> float:
        pass

    def get_vehicle(self) -> Vehicle:
        pass

    def get_external_costs(self) -> ExternalCosts:
        pass

    def get_internal_costs(self)-> InternalCosts:
        pass


# MvgSegments are created automatically, when MvgTrip is created. Segments are part of the Mvg-Api output

# this is an abstract class for segments: List[segment] of a trip: trip
class AbstractRoutingSegment(AbstractSegment):

    def __receive_response(self, start_location: Location, end_location: Location, segment_type: AbstractSegmentType):
        pass

    def __calculate_distance(self):
        pass

    def __calculate_duration(self):
        pass

    def __calculate_waypoints(self):
        pass

