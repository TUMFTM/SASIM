from enum import Enum, auto

from classes.Enum.SegmentType import OtpSegmentType

class MovementType(Enum):
    CAR = auto()
    MOPED = auto()
    ESCOOTER = auto()
    MOTORBIKE = auto()
    BICYCLE = auto()
    WALK = auto()
    PT = auto()

def movement_type_to_otp_type(movement_type: MovementType) -> OtpSegmentType:
    if (movement_type == MovementType.WALK):
        return OtpSegmentType.WALK

    elif (movement_type == MovementType.BICYCLE):
        return OtpSegmentType.BICYCLE

    elif (movement_type == MovementType.MOTORBIKE):
        return OtpSegmentType.CAR

    elif (movement_type == MovementType.MOPED):
        return OtpSegmentType.CAR

    elif (movement_type == MovementType.ESCOOTER):
        return OtpSegmentType.BICYCLE

    elif (movement_type == MovementType.CAR):
        return OtpSegmentType.CAR

    else:
        print("kein passendes OtpSegment für MovementType gefunden")



