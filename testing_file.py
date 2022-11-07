from classes.Location import Location
from classes.Trip.SimpleOtpTrip import SimpleOtpTrip
from classes.Vehicle.IndividualVehicle import IndividualVehicle
from classes.Enum.VehicleType import IndividualVehicleType
from classes.Enum.PropulsionType import PropulsionType

loc1 = Location(address="Ansprengerstr. 22, München")
loc2 = Location(address="Arcisstr. 3, München")

vehicle1 = IndividualVehicle(vehicle_type=IndividualVehicleType.BICYCLE, propulsion_type=PropulsionType.ELECTRIC,
                             location=loc1)

trip1 = SimpleOtpTrip(start_location=loc1, end_location=loc2, vehicle=vehicle1)
trip2 = SharingTrip()

print(trip1.get_distance())
print(trip1.get_direct_distance())
