from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Costs.external_costs_helper import add_external_costs
from classes.Enum.PropulsionType import PropulsionType
from classes.Enum.SegmentType import MvgSegmentType
from classes.Enum.SharingCompany import SharingCompany
from classes.Enum.TripType import IntermodalTripType
from classes.Enum.VehicleType import IndividualVehicleType, UrbanPublicVehicleType
from classes.Location import Location
from classes.Segment import Segment
from classes.Trip.PublicTransportTrip import PublicTransportTrip
from classes.Trip.SharingTrip import SharingTrip
from classes.Trip.SimpleOtpTrip import SimpleOtpTrip
from classes.Trip.Trip import Trip
from classes.Vehicle.IndividualVehicle import IndividualVehicle
from classes.Vehicle.UrbanPublicVehicle import UrbanPublicVehicle
from engines.geo_functions import get_distance as get_direct_distance
from mobility_controllers.costs.internal_costs_helper import calculate_internal_costs


# this trip type is a public transit trip, but the first and last segment (to and from the station)
# can be switched by another mode. E.g. private bike + public transit + emmy e-moped sharing


class IntermodalTripA(Trip):

    def __init__(self, start_location: Location, end_location: Location, there_inter_mode: IntermodalTripType = None,
                 away_inter_mode: IntermodalTripType = None):
        self.__start_location = start_location
        self.__end_location = end_location
        self.__there_inter_mode = there_inter_mode
        self.__away_inter_mode = away_inter_mode

        self.__mvg_trip = PublicTransportTrip(self.__start_location, self.__end_location)

        self.__segments = self.__create_intermodal_new_segments(self.__mvg_trip)
        self.__external_costs = self.__calculate_external_costs()
        self.__internal_costs = self.__calculate_internal_costs(self.__mvg_trip)

    def get_duration(self):
        """
        no input
        :return: duration: float (in Minutes)
        """
        return float(sum(list(map(lambda x: x.get_duration(), self.__segments))))

    def get_distance(self):
        """
        no input
        :return: distance: float (in kilometers)
        """
        return float(sum(list(map(lambda x: x.get_distance(), self.__segments))))

    def get_direct_distance(self):
        direct_distance = get_direct_distance(self.__start_location.get_coordinates(),
                                              self.__end_location.get_coordinates()) / 1000
        return direct_distance

    def get_external_costs(self):
        return self.__external_costs

    def get_internal_costs(self):
        return self.__internal_costs

    def get_segments(self):
        return self.__segments

    def get_trip_type(self):
        pass

    def __calculate_external_costs(self):
        external_costs: ExternalCosts = ExternalCosts()
        for i in range(len(self.__segments)):
            i_external_costs = self.__segments[i].get_external_costs()

            external_costs = add_external_costs(
                external_costs=external_costs,
                i_external_costs=i_external_costs
            )

        return external_costs

    def __calculate_internal_costs(self, mvg_trip):

        vehicle_mvv = UrbanPublicVehicle(vehicle_type=UrbanPublicVehicleType.PT)
        vehicle_bicycle = self.__segments[0].get_vehicle()
        distance_bicycle = self.__segments[0].get_distance()
        tarif_zone = mvg_trip.get_tarif_zone()

        internal_costs_mvv = calculate_internal_costs(vehicle=vehicle_mvv, tarif_zone=tarif_zone)
        internal_costs_bike = calculate_internal_costs(vehicle=vehicle_bicycle, distance=distance_bicycle)

        internal_costs = InternalCosts(value=internal_costs_mvv + internal_costs_bike)

        return internal_costs

    def __create_intermodal_new_segments(self, mvg_trip):

        # 1. split up segments
        segments = mvg_trip.get_segments()

        new_segments = []

        # 2. create new segments for segments with type WALKING_THERE and WALK_AWAY segments
        if ((self.__there_inter_mode != None) or (self.__away_inter_mode != None)):
            for i in range(len(segments)):
                segment = segments[i]
                start_location_segment = segment.get_waypoints()[0]
                end_location_segment = segment.get_waypoints()[-1]

                if ((segment.get_pt_segment_type() == MvgSegmentType.WALK_THERE) and (self.__there_inter_mode != None)):

                    new_segment = self.__calculate_new_segment(self.__there_inter_mode, start_location_segment,
                                                               end_location_segment)
                    if (type(new_segment) == list):
                        new_segments.extend(new_segment)
                    else:
                        new_segments.append(new_segment)

                elif ((segment.get_pt_segment_type() == MvgSegmentType.WALK_AWAY) and (self.__away_inter_mode != None)):
                    new_segment = self.__calculate_new_segment(self.__away_inter_mode, start_location_segment,
                                                               end_location_segment)
                    if (type(new_segment) == list):
                        new_segments.extend(new_segment)
                    else:
                        new_segments.append(new_segment)

                else:
                    new_segments.append(segment)

        else:
            print(self.__there_inter_mode, self.__away_inter_mode)
            new_segments = segments
            print("no intermodal mobility options selected")

        return new_segments

    def __calculate_new_segment(self, mode: IntermodalTripType, start_location_segment: Location,
                                end_location_segment: Location) -> Segment:
        if (mode == IntermodalTripType.PRIVATE_BICYCLE):
            vehicle = IndividualVehicle(IndividualVehicleType.BICYCLE, PropulsionType.MUSCLE)
            trip = SimpleOtpTrip(start_location_segment, end_location_segment, vehicle)
            new_segments = trip.get_segments()

        elif (mode == IntermodalTripType.PRIVATE_EBICYCLE):
            vehicle = IndividualVehicle(IndividualVehicleType.BICYCLE, PropulsionType.ELECTRIC)
            trip = SimpleOtpTrip(start_location_segment, end_location_segment, vehicle)
            new_segments = trip.get_segments()

        elif (mode == IntermodalTripType.PRIVATE_ESCOOTER):
            vehicle = IndividualVehicle(IndividualVehicleType.ESCOOTER)
            trip = SimpleOtpTrip(start_location_segment, end_location_segment, vehicle)
            new_segments = trip.get_segments()

        elif (mode == IntermodalTripType.EMMY):
            trip = SharingTrip(start_location_segment, end_location_segment, SharingCompany.EMMY)
            new_segments = trip.get_segments()


        elif (mode == IntermodalTripType.TIER):
            trip = SharingTrip(start_location_segment, end_location_segment, SharingCompany.TIER)
            new_segments = trip.get_segments()

        elif (mode == IntermodalTripType.CAB):
            trip = SharingTrip(start_location_segment, end_location_segment, SharingCompany.CAB)
            new_segments = trip.get_segments()

        else:
            print("intermodal trip type " + str(mode) + " not valid")

            return None

        return new_segments
