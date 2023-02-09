import 'package:latlong2/latlong.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Costs/Costs.dart';

import 'Waypoint.dart';

class Segment {
  final double distance;
  final double duration;
  final List<Waypoint> waypoints;
  final Costs costs;
  final String mode;

  Segment(
      {required this.distance,
      required this.duration,
      required this.waypoints,
      required this.costs,
      required this.mode});

  List<LatLng> getWaypointInLagLng() {
    return (waypoints.map((e) => LatLng(e.lat, e.lon))).toList();
  }
}
