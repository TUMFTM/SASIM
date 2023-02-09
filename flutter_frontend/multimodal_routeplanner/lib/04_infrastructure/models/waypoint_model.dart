import 'package:latlong2/latlong.dart';

import '../../03_domain/entities/Waypoint.dart';

class WaypointModel extends Waypoint {
  WaypointModel({required double lat, required double lon})
      : super(lat: lat, lon: lon);

  factory WaypointModel.fromJson(Map<String, dynamic> json) {
    return WaypointModel(lat: json['lat'], lon: json['lon']);
  }
}
