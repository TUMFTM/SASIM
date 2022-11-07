from enum import Enum, auto


class VehicleType(Enum):
    pass

class IndividualVehicleType(VehicleType):
    CAR = "Car"
    MOPED = "Moped"
    ESCOOTER = "E-Scooter"
    MOTORBIKE = "Motorbike"
    BICYCLE = "Bicycle"
    WALK = "Walk"

class UrbanPublicVehicleType(VehicleType):
    UBAHN = "U-Bahn"
    SBAHN = "S-Bahn"
    BUS = "Bus"
    TRAM = "Tram"
    PT = "Public Transport"

class SharingVehicleType(VehicleType):
    EMMY = "Emmy"
    SHARENOW = "Sharenow"
    FLINKSTER = "Flinkster"
    TIER = "Tier"
    CAB = "Call a Bike"




