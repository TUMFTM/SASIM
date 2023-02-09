import 'package:http/http.dart' as http;
import 'dart:convert';
import '../../03_domain/entities/MobilityMode.dart';
import '../../03_domain/entities/Trip.dart';
import '../../03_domain/enums/MobilityModeEnum.dart';
import '../models/trip_model.dart';

/// requests a trip from Route Planner REST-Api
/// throws a server-exception if respond code is not 200
abstract class RouteRemoteDatasource {
  Future<Trip> getSingleRouteFromApi(
      {required String startInput,
      required String endInput,
      required MobilityMode mode});
}

class RouteRemoteDatasourceImpl implements RouteRemoteDatasource {
  final http.Client client = http.Client();

  @override
  Future<Trip> getSingleRouteFromApi(
      {required String startInput,
      required String endInput,
      required MobilityMode mode}) async {
    // TODO: implement getSingleRouteFromApi

    String modeString = mapMode(mode: mode);

    var url = "http://www.sasim.mcube-cluster.de/plattform?inputStartAddress=$startInput&inputEndAddress=$endInput&tripMode=$modeString";

    // var url =
    //     "https://vmrp-web-app.herokuapp.com/plattform?inputStartAddress=$startInput&inputEndAddress=$endInput&tripMode=$modeString";

    var headers = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "Content-Type",
      "Referrer-Policy": "no-referrer-when-downgrade"
    };

    final response = await client.get(Uri.parse(url), headers: headers);
    final responseBody = json.decode(response.body);

    //print(responseBody);
    return TripModel.fromJson(responseBody);
  }

  String mapMode({required MobilityMode mode}) {
    switch (mode.mode) {
      case MobilityModeEnum.bike:
        return 'BICYCLE';
      case MobilityModeEnum.ebike:
        return 'EBICYCLE';
      case MobilityModeEnum.car:
        return 'CAR';
      case MobilityModeEnum.ecar:
        return 'ECAR';
      case MobilityModeEnum.moped:
        return 'MOPED';
      case MobilityModeEnum.emoped:
        return 'EMOPED';
      case MobilityModeEnum.escooter:
        return 'ESCOOTER';

      case MobilityModeEnum.mvg:
        return 'PT';
      case MobilityModeEnum.intermodal:
        return 'INTERMODAL_PT_BIKE';

      case MobilityModeEnum.emmy:
        return 'EMMY';
      case MobilityModeEnum.tier:
        return 'TIER';
      case MobilityModeEnum.flinkster:
        return 'FLINKSTER';
      case MobilityModeEnum.sharenow:
        return 'SHARENOW';
      case MobilityModeEnum.cab:
        return 'CAB';

      case MobilityModeEnum.walk:
        return 'WALK';
      default:
        return '';
    }
  }
}
