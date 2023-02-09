import 'package:latlong2/latlong.dart';

class Waypoint {
  final double lat;
  final double lon;

  Waypoint({required this.lat, required this.lon});

  LatLng getLatLng() {
    return LatLng(lat, lon);
  }
}
