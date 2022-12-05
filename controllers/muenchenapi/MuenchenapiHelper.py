from model.enums.mode.TripMode import TripMode
from model.enums.mode.IndividualMode import IndividualMode
from enum import Enum


class MuenchenapiMode(Enum):
    WALK = 'walk'
    CAR = 'car'
    BIKE = 'bike'
    INTERMODAL = 'intermodal'
    PUBLIC_TRANSPORT = 'public_transport'


class MuenchenapiHelper:

    def get_muenchenapi_mode_from_mode(self, mode: TripMode) -> MuenchenapiMode or None:

        if (mode == TripMode.WALK):
            return MuenchenapiMode.WALK

        elif (mode == TripMode.CAR or mode == TripMode.ECAR or mode == TripMode.MOPED or
              mode == TripMode.EMOPED or mode == TripMode.FLINKSTER or mode == TripMode.SHARENOW or mode == TripMode.EMMY):
            return MuenchenapiMode.CAR

        elif (mode == TripMode.BICYCLE or mode == TripMode.EBICYCLE or mode == TripMode.TIER):
            return MuenchenapiMode.BIKE

        elif (mode == TripMode.PT):
            return MuenchenapiMode.PUBLIC_TRANSPORT

        elif (mode == TripMode.INTERMODAL_PT_BIKE):
            return MuenchenapiMode.INTERMODAL

        else:
            print("ERROR: TripMode cannot be transformed to MuenchenapiMode")
            return None
