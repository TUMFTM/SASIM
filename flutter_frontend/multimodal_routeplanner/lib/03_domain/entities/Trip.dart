import 'package:multimodal_routeplanner/03_domain/entities/Costs/Costs.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Segment.dart';

import 'MobilityMode.dart';

class Trip {
  final double distance;
  final double duration;
  final Costs costs;
  final List<Segment> segments;
  final String mode;
  final String mobiScore;

  Trip(
      {required this.distance,
      required this.duration,
      required this.costs,
      required this.segments,
      required this.mode,
      required this.mobiScore});
}
