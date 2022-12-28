from enum import Enum

from model.entities.location.Location import Location
from model.enums.mode.IndividualMode import IndividualMode
from model.enums.mode.PublicTransportMode import PublicTransportMode
from model.enums.mode.SharingMode import SharingMode


class OtpHelper:

    def mode_to_otp_mode(self, mode: IndividualMode or PublicTransportMode or SharingMode):

        if(
                mode == IndividualMode.CAR or mode == IndividualMode.ECAR or mode == IndividualMode.MOPED or
                mode == IndividualMode.EMOPED or mode == SharingMode.EMMY or mode == SharingMode.FLINKSTER or
                mode == SharingMode.SHARENOW
        ):
            otp_mode = OtpMode.CAR

        elif(mode == IndividualMode.BICYCLE or mode == IndividualMode.EBICYCLE or
             mode == SharingMode.CAB or mode == SharingMode.TIER):
            otp_mode = OtpMode.BICYCLE

        elif(mode == IndividualMode.WALK):
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
