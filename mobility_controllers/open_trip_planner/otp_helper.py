from classes.Enum.SegmentType import OtpSegmentType
from classes.Enum.VehicleType import IndividualVehicleType

# needed to convert the mobility options to the 3 options in open trip planner (WALK, BICYCLE, CAR)
def vehicle_to_otp_type(vehicle_type: IndividualVehicleType) -> OtpSegmentType or None:
    if (vehicle_type == IndividualVehicleType.WALK):
        return OtpSegmentType.WALK

    elif (vehicle_type == IndividualVehicleType.BICYCLE):
        return OtpSegmentType.BICYCLE

    elif (vehicle_type == IndividualVehicleType.MOTORBIKE):
        return OtpSegmentType.CAR

    elif (vehicle_type == IndividualVehicleType.MOPED):
        return OtpSegmentType.CAR

    elif (vehicle_type == IndividualVehicleType.ESCOOTER):
        return OtpSegmentType.BICYCLE

    elif (vehicle_type == IndividualVehicleType.CAR):
        return OtpSegmentType.CAR

    else:
        print("kein passendes OtpSegment für MovementType gefunden")
        return None