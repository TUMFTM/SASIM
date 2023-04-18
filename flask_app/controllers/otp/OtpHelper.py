from enum import Enum

from model.entities.location.Location import Location
from model.enums.mode.TripMode import TripMode


class OtpHelper:

    def mode_to_otp_mode(self, mode: TripMode):

        if (
                mode == TripMode.CAR or mode == TripMode.ECAR or mode == TripMode.MOPED or
                mode == TripMode.EMOPED or mode == TripMode.EMMY or mode == TripMode.FLINKSTER or
                mode == TripMode.SHARENOW
        ):
            otp_mode = OtpMode.CAR

        elif (mode == TripMode.BICYCLE or mode == TripMode.EBICYCLE or
              mode == TripMode.CAB or mode == TripMode.TIER):
            otp_mode = TripMode.BICYCLE

        elif (mode == TripMode.WALK):
            otp_mode = OtpMode.WALK

        else:
            print("ERROR: mode cannot be tranlated to OTP-Modes")
            return 0

        return otp_mode

    def location_to_otp_format(self, location: Location):
        otp_location = (str(location.lat) + ", " + str(location.lon))
        return otp_location

class OtpMode(Enum):
    WALK = 'WALK'
    CAR = 'CAR'
    BICYCLE = 'BICYCLE'
