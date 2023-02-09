import 'package:multimodal_routeplanner/04_infrastructure/models/costs_model.dart';
import 'package:multimodal_routeplanner/04_infrastructure/models/segment_model.dart';

import '../../03_domain/entities/Costs/Costs.dart';
import '../../03_domain/entities/Segment.dart';
import '../../03_domain/entities/Trip.dart';

class TripModel extends Trip {
  TripModel(
      {required double distance,
      required double duration,
      required Costs costs,
      required List<Segment> segments,
      required String mode,
      required String mobiScore})
      : super(
            distance: distance,
            duration: duration,
            costs: costs,
            segments: segments,
            mode: mode,
            mobiScore: mobiScore);

  factory TripModel.fromJson(Map<String, dynamic> json) {
    return TripModel(
        distance: json['distance'] / 1000,
        duration: json['duration'],
        // costs: CostsModel.fromJson(json['costs']));
        costs: CostsModel.fromJson(json['costs']),
        segments: List<SegmentModel>.from(
            json['segments'].map((x) => SegmentModel.fromJson(x))),
        mode: json['tripMode'],
        mobiScore: json['mobiScore']);
  }
}
