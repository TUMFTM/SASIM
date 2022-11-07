from classes.Enum.PropulsionType import PropulsionType
from classes.Enum.SharingCompany import SharingCompany
from classes.Enum.TripType import IntermodalTripType
from classes.Enum.VehicleType import IndividualVehicleType
from classes.Location import Location
from classes.Trip.IntermodalTrip import IntermodalTripA
from classes.Trip.PublicTransportTrip import PublicTransportTrip
from classes.Trip.SharingTrip import SharingTrip
from classes.Trip.SimpleOtpTrip import SimpleOtpTrip
from classes.Vehicle.IndividualVehicle import IndividualVehicle


def get_single_trip_from_address(start_address: str, end_address: str, mode: str):
    start_location = Location(address=start_address)
    end_location = Location(address=end_address)

    trip = get_trip(mode, start_location, end_location)
    return trip


def get_trip(mode: str, start_location: Location, end_location: Location):

    #if-else statements for each available mobility option

    if (mode == "BIKE"):
        my_bicycle = IndividualVehicle(vehicle_type=IndividualVehicleType.BICYCLE,
                                       propulsion_type=PropulsionType.MUSCLE)
        trip = SimpleOtpTrip(start_location, end_location, my_bicycle)

    elif (mode == "EBIKE"):
        my_ebicycle = IndividualVehicle(vehicle_type=IndividualVehicleType.BICYCLE,
                                        propulsion_type=PropulsionType.ELECTRIC)
        trip = SimpleOtpTrip(start_location, end_location, my_ebicycle)

    elif (mode == "WALK"):
        my_walker = IndividualVehicle(vehicle_type=IndividualVehicleType.WALK,
                                      propulsion_type=PropulsionType.MUSCLE)
        trip = SimpleOtpTrip(start_location, end_location, my_walker)

    elif (mode == "CAR"):
        my_car = IndividualVehicle(vehicle_type=IndividualVehicleType.CAR, propulsion_type=PropulsionType.PETROL)
        trip = SimpleOtpTrip(start_location, end_location, my_car)

    elif (mode == "ECAR"):
        my_ecar = IndividualVehicle(vehicle_type=IndividualVehicleType.CAR, propulsion_type=PropulsionType.ELECTRIC)
        trip = SimpleOtpTrip(start_location, end_location, my_ecar)

    elif (mode == "MOPED"):
        my_moped = IndividualVehicle(vehicle_type=IndividualVehicleType.MOPED, propulsion_type=PropulsionType.PETROL)
        trip = SimpleOtpTrip(start_location, end_location, my_moped)

    elif (mode == "EMOPED"):
        my_emoped = IndividualVehicle(vehicle_type=IndividualVehicleType.MOPED, propulsion_type=PropulsionType.ELECTRIC)
        trip = SimpleOtpTrip(start_location, end_location, my_emoped)

    elif (mode == "ESCOOTER"):
        my_escooter = IndividualVehicle(vehicle_type=IndividualVehicleType.ESCOOTER,
                                        propulsion_type=PropulsionType.ELECTRIC)
        trip = SimpleOtpTrip(start_location, end_location, my_escooter)

    elif (mode == "MVG"):
        trip = PublicTransportTrip(start_location, end_location)

    elif (mode == "CAB"):
        trip = SharingTrip(start_location, end_location, SharingCompany.CAB)

    elif (mode == "SHARENOW"):
        trip = SharingTrip(start_location, end_location, SharingCompany.SHARENOW)

    elif (mode == "FLINKSTER"):
        trip = SharingTrip(start_location, end_location, SharingCompany.FLINKSTER)

    elif (mode == "EMMY"):
        trip = SharingTrip(start_location, end_location, SharingCompany.EMMY)

    elif (mode == "TIER"):
        trip = SharingTrip(start_location, end_location, SharingCompany.TIER)

    elif (mode == "INTERMODAL_BIKE"):
        trip = IntermodalTripA(start_location, end_location, there_inter_mode=IntermodalTripType.PRIVATE_BICYCLE)

    elif (mode == "INTERMODAL_CAB"):
        trip = IntermodalTripA(start_location, end_location, there_inter_mode=IntermodalTripType.CAB,
                               away_inter_mode=IntermodalTripType.CAB)

    else:
        print("trip mode is not valid")
        trip = None

    return trip
