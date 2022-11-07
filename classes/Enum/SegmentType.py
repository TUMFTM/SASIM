from dataclasses import dataclass
from enum import Enum, auto

class AbstractSegmentType(Enum):
    pass

class OtpSegmentType(AbstractSegmentType):
    WALK = 'WALK'
    CAR = 'CAR'
    BICYCLE = 'BICYCLE'

#TODO: weitere hinzufügen
class MvgSegmentType(AbstractSegmentType):
    INTERCHANGE = auto()
    WALK_THERE = auto()
    WALK_AWAY = auto()
    TRANSPORTATION = auto()
