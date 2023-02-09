import 'package:multimodal_routeplanner/04_infrastructure/models/waypoint_model.dart';

import '../../03_domain/entities/Costs/Costs.dart';
import '../../03_domain/entities/Segment.dart';
import '../../03_domain/entities/Waypoint.dart';
import 'costs_model.dart';

class SegmentModel extends Segment {
  SegmentModel({
    required double distance,
    required double duration,
    required List<Waypoint> waypoints,
    required Costs costs,
    required String mode,
  }) : super(
            costs: costs,
            distance: distance,
            duration: duration,
            waypoints: waypoints,
            mode: mode);

  factory SegmentModel.fromJson(Map<String, dynamic> json) {
    return SegmentModel(
        distance: json['distance'] / 1000,
        duration: json['duration'],
        costs: CostsModel.fromJson(json['costs']),
        waypoints: List<WaypointModel>.from(
            json['waypoints'].map((x) => WaypointModel.fromJson(x))),
        mode: json['mode']);
  }
}
