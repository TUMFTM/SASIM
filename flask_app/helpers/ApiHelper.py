from model.enums.mode.TripMode import TripMode


class ApiHelper:

    def get_trip_mode_from_input(self, trip_mode: str):

        if (trip_mode == 'WALK'):
            return TripMode.WALK

        elif (trip_mode == 'BICYCLE'):
            return TripMode.BICYCLE

        elif (trip_mode == 'EBICYCLE'):

            return TripMode.EBICYCLE

        elif (trip_mode == 'MOPED'):
            return TripMode.MOPED

        elif (trip_mode == 'EMOPED'):
            return TripMode.EMOPED

        elif (trip_mode == 'CAR'):
            return TripMode.CAR

        elif (trip_mode == 'ECAR'):
            return TripMode.ECAR


        elif (trip_mode == 'SHARENOW'):
            return TripMode.SHARENOW

        elif (trip_mode == 'FLINKSTER'):
            return TripMode.FLINKSTER

        elif (trip_mode == 'CAB'):
            return TripMode.CAB

        elif (trip_mode == 'EMMY'):
            return TripMode.EMMY

        elif (trip_mode == 'TIER'):
            return TripMode.TIER


        elif (trip_mode == 'PT'):
            return TripMode.PT

        elif (trip_mode == 'INTERMODAL_PT_BIKE'):
            return TripMode.INTERMODAL_PT_BIKE



        else:
            print("ERROR: mode input cannot be converted to variable type 'Mode'")
            return None
