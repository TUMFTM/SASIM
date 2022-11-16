from AA_new.enums.mode.IndividualMode import IndividualMode
from AA_new.enums.mode.PublicTransportMode import PublicTransportMode
from AA_new.enums.mode.SharingMode import SharingMode
from AA_new.enums.trip_type.TripType import TripType


class ApiHelper:

    def get_mode_from_input(self, mode: str):

        if(mode == 'WALK'):
            return IndividualMode.WALK

        elif(mode == 'BICYCLE'):
            return IndividualMode.BICYCLE

        elif (mode == 'EBICYCLE'):
            return IndividualMode.EBICYCLE

        elif (mode == 'MOPED'):
            return IndividualMode.MOPED

        elif (mode == 'EMOPED'):
            return IndividualMode.EMOPED

        elif (mode == 'CAR'):
            return IndividualMode.CAR

        elif (mode == 'ECAR'):
            return IndividualMode.ECAR

        elif (mode == 'CAB'):
            return SharingMode.CAB

        elif (mode == 'TIER'):
            return SharingMode.TIER

        elif (mode == 'EMMY'):
            return SharingMode.EMMY

        elif (mode == 'FLINKSTER'):
            return SharingMode.FLINKSTER

        elif (mode == 'SHARENOW'):
            return SharingMode.SHARENOW

        elif(mode == 'PT'):
            return PublicTransportMode.PT

        else:
            print("ERROR: mode input cannot be converted to variable type 'Mode'")
            return None

    def get_trip_type_from_input(self, trip_type: str):

        if (trip_type == 'TYPE_1'):
            return TripType.TYPE_1

        elif (trip_type == 'TYPE_2'):
            return TripType.TYPE_2

        elif (trip_type == 'TYPE_3'):
            return TripType.TYPE_3

        elif (trip_type == 'TYPE_4'):
            return TripType.TYPE_4

        else:
            print("ERROR: mode input cannot be converted to variable type 'TripType'")
            return None