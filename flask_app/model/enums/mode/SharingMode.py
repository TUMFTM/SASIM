from model.enums.mode.Mode import Mode


class SharingMode(Mode):
    CAB = 'CAB'
    TIER = 'TIER'
    EMMY = 'EMMY'
    FLINKSTER = 'FLINKSTER'
    SHARENOW = 'SHARENOW'

    ESCOOTER_SHARING = 'ESCOOTER_SHARING'
    MOPED_SHARING = 'MOPED_SHARING'
    BICYCLE_SHARING = 'BICYCLE_SHARING'
    CAR_SHARING = 'CAR_SHARING'


# class CarSharing(SharingMode):
#     FLINKSTER = 'FLINKSTER'
#     SHARENOW = 'SHARENOW'
#     STATTAUTO = 'STATTAUTO'
#
#
# class EscooterSharing(SharingMode):
#     TIER = 'TIER_BIKE'
#     VOI = 'VOI'
#
#
# class MopedSharing(SharingMode):
#     EMMY = 'EMMY'
#     TIER = 'TIER_MOPED'
#
#
# class BikeSharing(SharingMode):
#     CAB = 'CAB'
#     MVG_BIKE = 'MVG_BIKE'
#
#
# class EBikeSharing(SharingMode):
#     pass