import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:multimodal_routeplanner/03_domain/entities/MobilityMode.dart';
import '../../03_domain/enums/MobilityModeEnum.dart';

class ModeMappingHelper {
  MobilityModeEnum mapModeStringToMode(String mode) {
    switch (mode) {
      case 'WALK':
        return MobilityModeEnum.walk;

      case 'CAR':
        return MobilityModeEnum.car;

      case 'BICYCLE':
        return MobilityModeEnum.bike;

      case 'MOPED':
        return MobilityModeEnum.moped;

      case 'ECAR':
        return MobilityModeEnum.ecar;

      case 'EBICYCLE':
        return MobilityModeEnum.ebike;

      case 'EMOPED':
        return MobilityModeEnum.emoped;

      case 'CAB':
        return MobilityModeEnum.cab;

      case 'EMMY':
        return MobilityModeEnum.emmy;

      case 'TIER':
        return MobilityModeEnum.tier;

      case 'FLINKSTER':
        return MobilityModeEnum.flinkster;

      case 'SHARENOW':
        return MobilityModeEnum.sharenow;

      case 'PT':
        return MobilityModeEnum.mvg;

      case 'INTERMODAL_PT_BIKE':
        return MobilityModeEnum.intermodal;

      default:
        return MobilityModeEnum.bike;
    }
  }

  String mapModeToStringMode(MobilityMode mode){
    switch (mode.mode) {
      case MobilityModeEnum.walk:
        return 'WALK';

      case MobilityModeEnum.car:
        return 'CAR';

      case MobilityModeEnum.bike:
        return 'BICYCLE';

      case MobilityModeEnum.moped:
        return 'MOPED';

      case MobilityModeEnum.ecar:
        return 'ECAR';

      case MobilityModeEnum.ebike:
        return 'EBICYCLE';

      case MobilityModeEnum.emoped:
        return 'EMOPED';

      case MobilityModeEnum.cab:
        return 'CAB';

      case MobilityModeEnum.emmy:
        return 'EMMY';

      case MobilityModeEnum.tier:
        return 'TIER';

      case MobilityModeEnum.flinkster:
        return 'FLINKSTER';

      case MobilityModeEnum.sharenow:
        return 'SHARENOW';

      case MobilityModeEnum.mvg:
        return 'PT';

      case MobilityModeEnum.intermodal:
        return 'INTERMODAL_PT_BIKE';

      default:
        return 'BICYCLE';
    }
  }

  mapModeStringToIcon(String mode) {
    switch (mode) {
      case 'WALK':
        return const Icon(Icons.directions_walk);

      case 'CAR':
        return const Icon(Icons.directions_car);

      case 'BICYCLE':
        return const Icon(Icons.directions_bike);

      case 'MOPED':
        return const Icon(Icons.moped);

      case 'ECAR':
        return const Icon(
          Icons.electric_car,
        );

      case 'EBICYCLE':
        return const Icon(
          Icons.electric_bike,
        );

      case 'EMOPED':
        return const Icon(
          Icons.electric_moped,
        );

      case 'CAB':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_cab.png'),
        );

      case 'EMMY':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_emmy.png'),
        );

      case 'TIER':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_tier.jpg'),
        );

      case 'FLINKSTER':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_flinkster.png'),
        );

      case 'SHARENOW':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_sharenow.jpg'),
        );

      case 'PT':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_mvv.png'),
        );

      case 'INTERMODAL_PT_BIKE':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_mvv_plus_bike.png'),
        );

      default:
        return const Icon(
          Icons.electric_car,
        );
    }
  }

  mapModeStringToBigIcon(String mode) {
    switch (mode) {
      case 'WALK':
        return const Icon(Icons.directions_walk);

      case 'CAR':
        return const Icon(Icons.directions_car);

      case 'BICYCLE':
        return const Icon(Icons.directions_bike);

      case 'MOPED':
        return const Icon(Icons.moped);

      case 'ECAR':
        return const Icon(
          Icons.electric_car,
        );

      case 'EBICYCLE':
        return const Icon(
          Icons.electric_bike,
        );

      case 'EMOPED':
        return const Icon(
          Icons.electric_moped,
        );

      case 'CAB':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_cab.png'),
        );

      case 'EMMY':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_emmy.png'),
        );

      case 'TIER':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_tier.jpg'),
        );

      case 'FLINKSTER':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_flinkster.png'),
        );

      case 'SHARENOW':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_sharenow.jpg'),
        );

      case 'PT':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_mvv.png'),
        );

      case 'INTERMODAL_PT_BIKE':
        return const CircleAvatar(
          backgroundImage: AssetImage('assets/icons/icon_mvv_plus_bike.png'),
        );

      default:
        return const Icon(
          Icons.electric_car,
        );
    }
  }

  String mapModeStringToToolTip(String mode) {
    switch (mode) {
      case 'WALK':
        return 'zu Fuß';

      case 'CAR':
        return 'Pkw';

      case 'BICYCLE':
        return 'Fahrrad';

      case 'MOPED':
        return 'Moped';

      case 'ECAR':
        return 'E-Pkw';

      case 'EBICYCLE':
        return 'E-Fahrrad';

      case 'EMOPED':
        return 'E-Moped';

      case 'CAB':
        return 'Call a Bike';

      case 'EMMY':
        return 'Emmy';

      case 'TIER':
        return 'Tier';

      case 'FLINKSTER':
        return 'Flinkster';

      case 'SHARENOW':
        return 'Sharenow';

      case 'PT':
        return 'ÖPNV';

      case 'INTERMODAL_PT_BIKE':
        return 'ÖPNV + Fahrrad';

      default:
        return 'nicht vorhanden';
    }
  }

  AssetImage mapMobiScoreStringToPath(String mobiScore) {
    switch (mobiScore) {
      case 'A':
        return const AssetImage('assets/mobiscore/mobiscore_a.png');

      case 'B':
        return const AssetImage('assets/mobiscore/mobiscore_b.png');

      case 'C':
        return const AssetImage('assets/mobiscore/mobiscore_c.png');

      case 'D':
        return const AssetImage('assets/mobiscore/mobiscore_d.png');

      case 'E':
        return const AssetImage('assets/mobiscore/mobiscore_e.png');

      default:
        return const AssetImage('assets/mobiscore/mobiscore_e.png');
    }
  }
}
