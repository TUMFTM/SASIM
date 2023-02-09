import '../enums/MobilityModeEnum.dart';

class MobilityMode {
  final MobilityModeEnum mode;

  MobilityMode({required this.mode});

  MobilityModeEnum mapToMobilityModeEnum(String mode) {
    switch (mode) {
      case 'BICYCLE':
        return MobilityModeEnum.bike;

      case 'EBICYCLE':
        return MobilityModeEnum.ebike;

      case 'CAR':
        return MobilityModeEnum.car;

      case 'ECAR':
        return MobilityModeEnum.ecar;

      case 'MOPED':
        return MobilityModeEnum.moped;

      case 'EMOPED':
        return MobilityModeEnum.emoped;

      case 'ESCOOTER':
        return MobilityModeEnum.escooter;

      case 'PT':
        return MobilityModeEnum.mvg;

      case 'CAB':
        return MobilityModeEnum.cab;

      case 'FLINKSTER':
        return MobilityModeEnum.flinkster;

      case 'EMMY':
        return MobilityModeEnum.emmy;

      case 'TIER':
        return MobilityModeEnum.tier;

      case 'SHARENOW':
        return MobilityModeEnum.sharenow;

      case 'INTERMODAL_PT_BIKE':
        return MobilityModeEnum.intermodal;

      default:
        return MobilityModeEnum.bike;
    }
  }
}
