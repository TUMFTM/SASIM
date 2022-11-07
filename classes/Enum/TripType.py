from enum import Enum, auto

#TODO: add more trip types

class TripType(Enum):
    # private vehicles
    CAR = auto()
    ECAR = auto()
    BICYCLE = auto()
    EBICYCLE = auto()
    MOPED = auto()
    EMOPED = auto()
    ESCOOTER = auto()
    WALK = auto()

    # sharing vehicles
    CARSHARING = auto()
    ECARSHARING = auto()
    BICYCLESHARING = auto()
    EBICYCLESHARING = auto()
    EMOPEDSHARING = auto()
    ESCOOTERSHARING = auto()

    # sharing services
    EMMY = auto()
    TIER = auto()
    CAB = auto()
    FLINKSTER = auto()
    DRIVENOW = auto()

    # general trip types
    SIMPLE = auto()
    SHARING = auto()
    MVG = auto()

class IntermodalTripType(Enum):
    PRIVATE_BICYCLE = auto()
    PRIVATE_EBICYCLE = auto()
    PRIVATE_ESCOOTER = auto()

    # sharing services
    EMMY = auto()
    TIER = auto()
    CAB = auto()
