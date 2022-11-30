from controllers.costs.CostsController import CostsController
from controllers.mobi_score.MobiScoreController import MobiScoreController
from controllers.mvv.MvvController import MvvController
from controllers.otp.OtpController import OtpController
from controllers.sharing.EmmyController import EmmyController
from controllers.sharing.ShareNowController import ShareNowController
from controllers.sharing.TierController import TierController
from controllers.sharing.deutsche_bahn.CallABikeController import CallABikeController
from controllers.sharing.deutsche_bahn.FlinksterController import FlinksterController
from model.entities.costs.Costs import Costs
from model.entities.costs.ExternalCosts import ExternalCosts
from model.entities.costs.InternalCosts import InternalCosts
from model.entities.location.Location import Location
from model.entities.segment.IndividualSegment import IndividualSegment
from model.entities.segment.PublicTransportSegment import PublicTransportSegment
from model.entities.segment.SharingSegment import SharingSegment
from model.entities.trip.Trip import Trip
from model.enums.mode.IndividualMode import IndividualMode
from model.enums.mode.Mode import Mode
from model.enums.mode.SharingMode import SharingMode
from model.enums.mode.TripMode import TripMode
from model.enums.trip_type.TripType import TripType
from helpers.GeoHelper import GeoHelper


class TripController:
    def __init__(self):

        self._otp_controller = OtpController()
        self._mvv_controller = MvvController()

        self._emmy_controller = EmmyController()
        self._share_now_controller = ShareNowController()
        self._tier_controller = TierController()
        self._call_a_bike_controller = CallABikeController()
        self._flinkster_controller = FlinksterController()

        self._costs_controller = CostsController()
        self._mobi_score_controller = MobiScoreController()

        self._geo_helper = GeoHelper()

    def get_trip(self, start_location: Location, end_location: Location, trip_mode: TripMode) -> Trip:

        trip_type = self._get_trip_type_from_trip_mode(trip_mode=trip_mode)

        if (trip_type == TripType.TYPE_1):

            mode = self._get_mode_from_trip_mode(trip_mode=trip_mode)

            trip = self._get_trip_type_1(start_location=start_location, end_location=end_location, mode=mode,
                                         trip_mode=trip_mode)

        elif (trip_type == TripType.TYPE_2):

            mode = self._get_mode_from_trip_mode(trip_mode=trip_mode)

            trip = self._get_trip_type_2(start_location=start_location, end_location=end_location, sharing_mode=mode,
                                         trip_mode=trip_mode)

        elif (trip_type == TripType.TYPE_3):
            trip = self._get_trip_type_3_4(start_location=start_location, end_location=end_location,
                                           trip_type=TripType.TYPE_3, trip_mode=trip_mode)

        elif (trip_type == TripType.TYPE_4):
            trip = self._get_trip_type_3_4(start_location=start_location, end_location=end_location,
                                           trip_type=TripType.TYPE_4, trip_mode=trip_mode)

        else:
            print("Error: trip type now valid")
            trip = None

        return trip

    def _get_trip_type_1(self, start_location: Location, end_location: Location, mode: IndividualMode,
                         trip_mode: TripMode):

        otp_response = self._otp_controller.otp_request(
            input_startloc=start_location,
            input_endloc=end_location,
            mode=mode
        )

        waypoints = self._otp_controller.get_waypoints(otp_response)
        duration = self._otp_controller.get_duration(otp_response)
        distance = self._otp_controller.get_distance(otp_response)

        external_costs = self._costs_controller.get_external_costs(
            distance=distance,
            mode=mode
        )

        internal_costs = self._costs_controller.get_internal_costs(
            distance=distance,
            duration=duration,
            mode=mode
        )

        costs = Costs(
            internal_costs=internal_costs,
            external_costs=external_costs
        )

        segment = IndividualSegment(
            mode=mode,
            duration=duration,
            distance=distance,
            costs=costs,
            waypoints=waypoints
        )

        direct_distance = self._geo_helper.get_distance(start_location=start_location, end_location=end_location)
        mobi_score = self._mobi_score_controller.get_mobi_score(
            segment.costs.external_costs,
            direct_distance=direct_distance
        )

        trip = Trip(
            start_location=start_location,
            end_location=end_location,
            trip_mode=trip_mode,
            segments=[segment],
            duration=segment.duration,
            distance=segment.distance,
            costs=segment.costs,
            mobi_score=mobi_score
        )

        return trip

    def _get_trip_type_2(self, start_location: Location, end_location: Location, sharing_mode: SharingMode,
                         trip_mode: TripMode):

        # 1. get sharing position
        location_closest_vehicle = self._get_sharing_position(start_location=start_location, sharing_mode=sharing_mode)

        # 2. get walk waypoints, distance, duration, costs
        otp_response_walk = self._otp_controller.otp_request(
            input_startloc=start_location,
            input_endloc=location_closest_vehicle,
            mode=IndividualMode.WALK
        )

        distance_walk = self._otp_controller.get_distance(response=otp_response_walk)
        duration_walk = self._otp_controller.get_duration(response=otp_response_walk)
        waypoints_walk = self._otp_controller.get_waypoints(response=otp_response_walk)
        internal_costs_walk = self._costs_controller.get_internal_costs(
            distance=distance_walk,
            duration=duration_walk,
            mode=IndividualMode.WALK
        )
        external_costs_walk = self._costs_controller.get_external_costs(distance=distance_walk,
                                                                        mode=IndividualMode.WALK)
        costs_walk = Costs(external_costs=external_costs_walk, internal_costs=internal_costs_walk)

        segment_walk = IndividualSegment(
            mode=IndividualMode.WALK,
            duration=duration_walk,
            distance=distance_walk,
            costs=costs_walk,
            waypoints=waypoints_walk
        )

        # 3. get ride waypoints, distance, duration, costs
        otp_response_ride = self._otp_controller.otp_request(
            input_startloc=location_closest_vehicle,
            input_endloc=end_location,
            mode=sharing_mode
        )

        distance_ride = self._otp_controller.get_distance(response=otp_response_ride)
        duration_ride = self._otp_controller.get_duration(response=otp_response_ride)
        waypoints_ride = self._otp_controller.get_waypoints(response=otp_response_ride)
        internal_costs_ride = self._costs_controller.get_internal_costs(
            distance=distance_ride,
            duration=duration_ride,
            mode=sharing_mode
        )

        external_costs_ride = self._costs_controller.get_external_costs(
            distance=distance_ride,
            mode=sharing_mode
        )

        costs_ride = Costs(external_costs=external_costs_ride, internal_costs=internal_costs_ride)

        segment_ride = SharingSegment(
            mode=sharing_mode,
            duration=duration_ride,
            distance=distance_ride,
            costs=costs_ride,
            waypoints=waypoints_ride
        )

        external_costs = external_costs_walk + external_costs_ride
        direct_distance = self._geo_helper.get_distance(start_location=start_location, end_location=end_location)
        mobi_score = self._mobi_score_controller.get_mobi_score(
            external_costs=external_costs,
            direct_distance=direct_distance
        )

        trip = Trip(
            start_location=start_location,
            end_location=end_location,
            trip_mode=trip_mode,
            segments=[segment_walk, segment_ride],
            duration=duration_walk + duration_ride,
            distance=distance_walk + distance_ride,
            costs=costs_walk + costs_ride,
            mobi_score=mobi_score
        )

        return trip

    def _get_trip_type_3_4(self, start_location: Location, end_location: Location, trip_type: TripType,
                           trip_mode: TripMode):

        mvv_response = self._mvv_controller.get_response(start_location=start_location, end_location=end_location)
        mvv_trip_data = self._mvv_controller.get_mvv_trip_data(mvv_response)

        segments = []
        total_distance = 0
        total_duration = 0
        total_internal_costs = InternalCosts()
        total_external_costs = ExternalCosts()

        for i in range(len(mvv_trip_data.mvv_trip)):

            if (trip_type == TripType.TYPE_4 and i == 0):

                end_location_bike = mvv_trip_data.mvv_trip[0].waypoints[-1]
                otp_response = self._otp_controller.otp_request(input_startloc=start_location,
                                                                input_endloc=end_location_bike,
                                                                mode=IndividualMode.BICYCLE)

                mode = IndividualMode.WALK
                duration = self._otp_controller.get_duration(otp_response)
                distance = self._otp_controller.get_distance(otp_response)
                waypoints = self._otp_controller.get_waypoints(otp_response)
                internal_costs = self._costs_controller.get_internal_costs(distance, duration, mode)
                external_costs = self._costs_controller.get_external_costs(distance, mode)
                costs = Costs(
                    internal_costs=internal_costs,
                    external_costs=external_costs
                )

                segments.append(IndividualSegment(
                    mode=mode,
                    duration=duration,
                    distance=distance,
                    costs=costs,
                    waypoints=waypoints
                ))

            else:
                mode = mvv_trip_data.mvv_trip[i].mode
                duration = mvv_trip_data.mvv_trip[i].duration
                distance = mvv_trip_data.mvv_trip[i].distance
                waypoints = mvv_trip_data.mvv_trip[i].waypoints
                from_tarif_zone = mvv_trip_data.mvv_trip[i].from_tarif_zone
                to_tarif_zone = mvv_trip_data.mvv_trip[i].to_tarif_zone

                external_costs = self._costs_controller.get_external_costs(distance, mode)
                internal_costs = InternalCosts(internal_costs=0)

                costs = Costs(
                    internal_costs=internal_costs,
                    external_costs=external_costs
                )

                segments.append(PublicTransportSegment(
                    mode=mode,
                    duration=duration,
                    distance=distance,
                    costs=costs,
                    waypoints=waypoints,
                    from_tarif_zone=from_tarif_zone,
                    to_tarif_zone=to_tarif_zone
                ))

            total_distance += distance
            total_duration += duration
            total_internal_costs += internal_costs
            total_external_costs += external_costs

        direct_distance = self._geo_helper.get_distance(start_location=start_location, end_location=end_location)
        mobi_score = self._mobi_score_controller.get_mobi_score(
            external_costs=total_external_costs,
            direct_distance=direct_distance
        )

        internal_trip_costs = self._costs_controller.get_internal_public_transport_costs(mvv_trip_data.mvv_ticket_name)
        total_costs = Costs(
            internal_costs=internal_trip_costs,
            external_costs=total_external_costs
        )

        trip = Trip(
            start_location=start_location,
            end_location=end_location,
            trip_mode=trip_mode,
            segments=segments,
            duration=total_duration,
            distance=total_distance,
            costs=total_costs,
            mobi_score=mobi_score
        )

        return trip

    def _get_sharing_position(self, sharing_mode: SharingMode, start_location: Location):

        if (sharing_mode == SharingMode.EMMY):
            closest_vehicle = self._emmy_controller.get_closest_vehicle(start_location)

        elif (sharing_mode == SharingMode.TIER):
            closest_vehicle = self._tier_controller.get_closest_vehicle(start_location)

        elif (sharing_mode == SharingMode.CAB):
            closest_vehicle = self._call_a_bike_controller.get_closest_vehicle(start_location)

        elif (sharing_mode == SharingMode.SHARENOW):
            closest_vehicle = self._share_now_controller.get_closest_vehicle(start_location)

        elif (sharing_mode == SharingMode.FLINKSTER):
            closest_vehicle = self._flinkster_controller.get_closest_vehicle(start_location)

        else:
            print("ERROR: sharing mode is not valid to find closest sharing vehicle")
            closest_vehicle = None

        return closest_vehicle

    def _get_trip_type_from_trip_mode(self, trip_mode: TripMode) -> TripType or None:

        if (
                trip_mode == TripMode.CAR or
                trip_mode == TripMode.ECAR or
                trip_mode == TripMode.MOPED or
                trip_mode == TripMode.EMOPED or
                trip_mode == TripMode.BICYCLE or
                trip_mode == TripMode.EBICYCLE or
                trip_mode == TripMode.WALK
        ):
            return TripType.TYPE_1

        elif (
                trip_mode == TripMode.CAB or
                trip_mode == TripMode.FLINKSTER or
                trip_mode == TripMode.SHARENOW or
                trip_mode == TripMode.TIER or
                trip_mode == TripMode.EMMY
        ):
            return TripType.TYPE_2

        elif (trip_mode == TripMode.PT):
            return TripType.TYPE_3
        elif (trip_mode == TripMode.INTERMODAL_PT_BIKE):
            return TripType.TYPE_4
        else:
            print("ERROR: trip mode not valid for conversion into trip type")
            return None

    def _get_mode_from_trip_mode(self, trip_mode: TripMode) -> Mode or None:
        if (trip_mode == TripMode.CAR):
            return IndividualMode.CAR
        elif (trip_mode == TripMode.ECAR):
            return IndividualMode.ECAR
        if (trip_mode == TripMode.MOPED): return IndividualMode.MOPED
        if (trip_mode == TripMode.EMOPED): return IndividualMode.EMOPED
        if (trip_mode == TripMode.BICYCLE): return IndividualMode.BICYCLE
        if (trip_mode == TripMode.EBICYCLE): return IndividualMode.EBICYCLE
        if (trip_mode == TripMode.WALK): return IndividualMode.WALK

        if (trip_mode == TripMode.CAB): return SharingMode.CAB
        if (trip_mode == TripMode.FLINKSTER): return SharingMode.FLINKSTER
        if (trip_mode == TripMode.SHARENOW): return SharingMode.SHARENOW
        if (trip_mode == TripMode.TIER): return SharingMode.TIER
        if (trip_mode == TripMode.EMMY):
            return SharingMode.EMMY

        else:
            print("ERROR: trip mode not valid for conversion into mode")
            return None

# ## TESTING
# # Ansprengerstr. 22
# lat1 = 48.1663834
# lon1 = 11.5748712
#
# # Sonnenstra. 11
# lat2 = 48.1377949
# lon2 = 11.5630753
#
# loc1 = Location(lat=lat1, lon=lon1)
# loc2 = Location(lat=lat2, lon=lon2)
#
# trip_controller = TripController()
# trip = trip_controller.get_trip(loc1, loc2, TripType.TYPE_4)
# trip_n = trip_controller.get_trip(loc1, loc2, TripType.TYPE_3)
# print("mobiscore: " + str(trip.mobi_score))
# print("distance: " + str(trip.distance))
# print("internal: " + str(trip.costs.internal_costs.internal_costs))
# print("external: " + str(trip.costs.external_costs.external_costs))
