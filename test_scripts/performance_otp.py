from classes.Enum.PropulsionType import PropulsionType
from classes.Enum.SharingCompany import SharingCompany
from classes.Enum.TripType import IntermodalTripType
from classes.Enum.VehicleType import IndividualVehicleType
from classes.Location import Location
from classes.Trip.IntermodalTrip import IntermodalTripA
from classes.Trip.PublicTransportTrip import PublicTransportTrip
from classes.Trip.SimpleOtpTrip import SimpleOtpTrip
from classes.Vehicle.IndividualVehicle import IndividualVehicle
from classes.Vehicle.SharingVehicle import SharingVehicle

# start_location = location(address="Arcisstraße 21, München")
# end_location = location(address="Emmy-Noether-Str. 2, München")

car = IndividualVehicle(IndividualVehicleType.CAR, PropulsionType.PETROL)
bicycle = IndividualVehicle(IndividualVehicleType.BICYCLE, PropulsionType.MUSCLE)
walker = IndividualVehicle(IndividualVehicleType.WALK, PropulsionType.MUSCLE)


locations = [
    # 0 SWM
    Location(address="Emmy-Noether-Str. 2, München"),

    # 1 Allianz Arena 1
    Location(address="Werner-Heisenberg-Allee 25, München"),

    # 2 Grünwald 2
    Location(address="Grünwalder Str. 2, München"),

    # 3 Dritter Orden
    Location(address="Menzinger Str. 44, München"),

    # 4 Pinas
    Location(address="Barer Str. 29, 80799 München"),

    # 5 MCi
    Location(address="Feilitzschstr. 13, München"),

    # 6 Westpark
    Location(address="Eduard-Stadler-Winkel 3, München"),
]


def while_simulation_loop(start_location, end_location):
    i = 0
    while i < 30:
        IntermodalTripA(start_location, end_location, there_inter_mode=IntermodalTripType.PRIVATE_BICYCLE)

        SimpleOtpTrip(start_location, end_location, car)
        SimpleOtpTrip(start_location, end_location, bicycle)
        SimpleOtpTrip(start_location, end_location, walker)

        SharingVehicle(start_location, SharingCompany.EMMY)
        SharingVehicle(start_location, SharingCompany.TIER)
        SharingVehicle(start_location, SharingCompany.SHARENOW)
        SharingVehicle(start_location, SharingCompany.FLINKSTER)
        SharingVehicle(start_location, SharingCompany.CAB)

        PublicTransportTrip(start_location, end_location)

        i = i + 1



while_simulation_loop(locations[0], locations[4])
while_simulation_loop(locations[4], locations[5])
while_simulation_loop(locations[6], locations[1])






