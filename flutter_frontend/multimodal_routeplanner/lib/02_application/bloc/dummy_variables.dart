/* import 'dart:html';

import 'package:latlong2/latlong.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Costs/Costs.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Costs/ExternalCosts.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Costs/InternalCosts.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Segment.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';
import 'package:multimodal_routeplanner/03_domain/enums/MobilityMode.dart';

class DummyVariables {
  final List<LatLng> waypoints1 = [
    LatLng(48.1663835, 11.5752574),
    LatLng(48.16708, 11.57919),
    LatLng(48.1671, 11.58015),
    LatLng(48.16738, 11.58838)
  ];
  final List<LatLng> waypoints2 = [
    LatLng(48.16736, 11.58854),
    LatLng(48.16511, 11.59333),
    LatLng(48.16155, 11.59891),
    LatLng(48.15637, 11.60299)
  ];
  final ExternalCosts externalCosts1 = ExternalCosts(
      air: 0.4,
      noise: 0.2,
      climate: 0.5,
      upstream: 1.0,
      accidents: 1.2,
      space: 0.7);
  final InternalCosts internalCosts1 = InternalCosts(internalCosts: 2.3);

  _getCosts() {
    return Costs(externalCosts: externalCosts1, internalCosts: internalCosts1);
  }

  getTrip({required String startInput, required String endInput}) {
    Costs costs = _getCosts();
    Segment segment1 = Segment(
        distance: 5.0,
        duration: 27.3,
        waypoints: waypoints1,
        costs: costs,
        mode: MobilityMode.walk);

    Segment segment2 = Segment(
        distance: 5.0,
        duration: 27.3,
        waypoints: waypoints2,
        costs: costs,
        mode: MobilityMode.bike);

    double tripDistance = segment1.distance + segment2.distance;
    double tripDuration = segment1.duration + segment2.duration;

    ExternalCosts tripExternalCosts = ExternalCosts(
        air: externalCosts1.air * 2,
        noise: externalCosts1.noise * 2,
        climate: externalCosts1.climate * 2,
        upstream: externalCosts1.upstream * 2,
        accidents: externalCosts1.accidents * 2,
        space: externalCosts1.space * 2,
        all: );

    InternalCosts tripInternalCosts =
        InternalCosts(internalCosts: internalCosts1.internalCosts * 2);

    Costs tripCosts = Costs(
        externalCosts: tripExternalCosts, internalCosts: tripInternalCosts);

    /* Trip trip1 =
        Trip(distance: tripDistance, duration: tripDuration, costs: tripCosts); */

    Trip trip1 =
        Trip(distance: tripDistance, duration: tripDuration, costs: 0.4356);
    return trip1;
  }
}
 */