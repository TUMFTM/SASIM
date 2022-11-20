from enum import Enum, auto

class TripType(Enum):
    TYPE_1 = auto() #trips with only one private vehicle
    TYPE_2 = auto() #trips with sharing vehicles, consisting of a walk-segment to the vehicle and a ride-segment
    TYPE_3 = auto() #trips with public transportation, starting with a walk to the nearest station
    TYPE_4 = auto() #trips with public transportation, starting with a bike-ride to the nearest station
