from classes.Enum.PropulsionType import PropulsionType
from classes.Enum.SegmentType import OtpSegmentType
from classes.Enum.SharingCompany import SharingCompany
from classes.Enum.VehicleType import IndividualVehicleType


def get_vehicle_type_for_sharing(sharing_company: SharingCompany) -> IndividualVehicleType:
    if(sharing_company == SharingCompany.EMMY):
        return IndividualVehicleType.MOPED
    elif(sharing_company == SharingCompany.CAB):
        return IndividualVehicleType.BICYCLE
    elif (sharing_company == SharingCompany.FLINKSTER):
        return IndividualVehicleType.CAR
    elif (sharing_company == SharingCompany.SHARENOW):
        return IndividualVehicleType.CAR
    elif (sharing_company == SharingCompany.TIER):
        return IndividualVehicleType.ESCOOTER
    else:
        print("Kein VehicleType für die Sharing Company: " + str(sharing_company))

def get_otp_segment_type_for_sharing(vehicle_type: IndividualVehicleType) -> OtpSegmentType:
    if (vehicle_type == IndividualVehicleType.MOPED):
        return OtpSegmentType.CAR
    elif (vehicle_type == IndividualVehicleType.CAR):
        return OtpSegmentType.CAR
    elif (vehicle_type == IndividualVehicleType.BICYCLE):
        return OtpSegmentType.BICYCLE
    elif (vehicle_type == IndividualVehicleType.MOTORBIKE):
        return OtpSegmentType.CAR
    elif (vehicle_type == IndividualVehicleType.ESCOOTER):
        return OtpSegmentType.BICYCLE

def get_propulsion_type_for_sharing(sharing_company: SharingCompany) -> PropulsionType:
    if (sharing_company == SharingCompany.EMMY):
        return PropulsionType.ELECTRIC

    elif (sharing_company == SharingCompany.CAB):
        return PropulsionType.MUSCLE

    elif (sharing_company == SharingCompany.FLINKSTER):
        return PropulsionType.PETROL

    elif (sharing_company == SharingCompany.SHARENOW):
        return PropulsionType.PETROL

    elif (sharing_company == SharingCompany.TIER):
        return PropulsionType.ELECTRIC