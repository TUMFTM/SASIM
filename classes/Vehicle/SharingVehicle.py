from classes.Enum.PropulsionType import PropulsionType
from classes.Enum.VehicleType import VehicleType
from mobility_controllers.mobility_api.sharing.sharing_helper import get_vehicle_type_for_sharing, get_otp_segment_type_for_sharing, \
    get_propulsion_type_for_sharing
from classes.Enum.SegmentType import OtpSegmentType
from classes.Enum.SharingCompany import SharingCompany
from classes.Vehicle.Vehicle import Vehicle
from classes.Location import Location
from mobility_controllers.mobility_api.sharing.db_controller import get_location_closest_cab_vehicle, get_location_closest_flinkster_vehicle
from mobility_controllers.mobility_api.sharing.emmy_controller import get_location_closest_emmy_vehicle
from mobility_controllers.mobility_api.sharing.sharenow_controller import get_location_closest_sharenow_vehicle
from mobility_controllers.mobility_api.sharing.tier_controller import get_location_closest_tier_vehicle


class SharingVehicle(Vehicle):

    def __init__(self, start_location: Location, company_name: SharingCompany):
        self.__start_location = start_location
        self.__company_name = company_name

        self.__location_closest_vehicle: Location = self.__find_location_closest_vehicle()


    def __find_location_closest_vehicle(self) -> Vehicle or None:

        if (self.__company_name == SharingCompany.EMMY):
            return get_location_closest_emmy_vehicle(self.__start_location)

        if (self.__company_name == SharingCompany.TIER):
            return get_location_closest_tier_vehicle(self.__start_location)

        if (self.__company_name == SharingCompany.CAB):
            return get_location_closest_cab_vehicle(self.__start_location)

        if (self.__company_name == SharingCompany.FLINKSTER):
            return get_location_closest_flinkster_vehicle(self.__start_location)

        if (self.__company_name == SharingCompany.SHARENOW):
            return get_location_closest_sharenow_vehicle(self.__start_location)

        else:
            print("Es existiert kein Fahrzeug dieser Marke")
            return None

    def get_location(self):
        return self.__location_closest_vehicle

    def get_vehicle_type(self) -> VehicleType:

        return(get_vehicle_type_for_sharing(self.__company_name))

    def get_company_name(self):
        return self.__company_name

    def get_otp_segment_type(self) -> OtpSegmentType:

        vehicle_type = self.get_vehicle_type()
        return (get_otp_segment_type_for_sharing(vehicle_type))

    def is_sharing(self) -> bool:
        return True

    def get_propulsion_type(self) -> PropulsionType:

        #TODO: fetch propulsion type from API or Database
        # DB could be -sharing_helper-

        sharing_company = self.get_company_name()
        return (get_propulsion_type_for_sharing(sharing_company))

