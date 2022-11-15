from AA_new.entities_new.location.Location import Location
from AA_new.entities_new.trip.Trip import Trip
from AA_new.enums.trip_type.TripType import TripType


class TripController:
    def __init__(self):
        pass

    def get_trip(self, start_location: Location, end_location: Location, mode: Mode, trip_type: TripType) -> Trip:
        pass

        if (trip_type == TripType.TYPE_1):
            pass

        elif (trip_type == TripType.TYPE_2):
            pass

        elif (trip_type == TripType.TYPE_3):
            pass

        elif (trip_type == TripType.TYPE_4):
            pass

        else:
            print("Error: trip type now valid")

        trip = Trip(
            start_location = start_location,
            end_location = end_location,
            trip_type = trip_type,
            segments = null,
            duration = null,
            distance = null,
            costs = null
        )


        return trip

    # TYPE 1
    def _get_trip_1(self):
        # 1. get otp information: duration, distance, waypoints
        # 2. costs
        pass

    def _get_individual_segment(self):
        pass

    def _get_pt_segments(self):
        pass

    def _get_costs(self):
        pass

