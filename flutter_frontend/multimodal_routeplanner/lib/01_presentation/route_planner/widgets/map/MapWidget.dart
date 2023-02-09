import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:flutter_map_tappable_polyline/flutter_map_tappable_polyline.dart';
import 'package:latlong2/latlong.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/map/StartMarker.dart';
import 'package:multimodal_routeplanner/02_application/bloc/visualization_bloc.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';
import 'package:multimodal_routeplanner/values.dart';


import 'StopMarker.dart';

class MapWidget extends StatelessWidget {
  const MapWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        BlocBuilder<VisualizationBloc, VisualizationState>(
          builder: (context, routePlannerState) {
            if (routePlannerState is VisualizationChangedState) {
              Trip selectedTrip = routePlannerState.selectedTrip;

              return FlutterMap(
                options: MapOptions(
                  plugins: [
                    TappablePolylineMapPlugin(),
                  ],
                  center: LatLng(48.1662627, 11.5768211),
                  zoom: 13.0,
                ),
                layers: [
                  TileLayerOptions(
                      urlTemplate:
                          "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                      subdomains: ['a', 'b', 'c']),
                  TappablePolylineLayerOptions(
                      polylineCulling: true,
                      polylines: [

                        // visualize selected
                        for (var i = 0; i < selectedTrip.segments.length; i++)
                          TaggedPolyline(
                            points:
                                selectedTrip.segments[i].getWaypointInLagLng(),
                            tag: "selected",
                            strokeWidth: 5,
                            color: mapSegmentModeToColor(
                                selectedTrip.segments[i].mode),
                          ),
                      ],
                      onTap: (polylines, tapPosition) => {},
                      onMiss: (tapPosition) {}),
                  MarkerLayerOptions(
                    markers: [
                      Marker(
                        point: selectedTrip.segments.first.waypoints.first
                            .getLatLng(),
                        builder: (ctx) => const StartMarker(),
                      ),
                      Marker(
                        point: selectedTrip.segments.last.waypoints.last
                            .getLatLng(),
                        builder: (ctx) => const StopMarker(),
                      ),
                      /*Marker(
                        width: 150,
                        height: 108,
                        point: fastestTrip.segments.length > 1
                            ? fastestTrip
                                .segments[1]
                                .waypoints[
                                    (fastestTrip.segments[1].waypoints.length /
                                            2)
                                        .ceil()]
                                .getLatLng()
                            : fastestTrip
                                .segments[0]
                                .waypoints[
                                    (fastestTrip.segments[0].waypoints.length /
                                            2)
                                        .ceil()]
                                .getLatLng(),
                        builder: (ctx) => RouteMarker(
                          trip: fastestTrip,
                          routeMarkerType: RouteMarkerType.fastest,
                        ),
                        anchorPos: AnchorPos.align(AnchorAlign.right),
                      ),
                      Marker(
                        width: 250,
                        height: 108,
                        point: lowestExternalCostsTrip.segments.length > 1
                            ? lowestExternalCostsTrip
                                .segments[1]
                                .waypoints[(lowestExternalCostsTrip
                                            .segments[1].waypoints.length /
                                        2)
                                    .ceil()]
                                .getLatLng()
                            : lowestExternalCostsTrip
                                .segments[0]
                                .waypoints[(lowestExternalCostsTrip
                                            .segments[0].waypoints.length /
                                        2)
                                    .ceil()]
                                .getLatLng(),
                        builder: (ctx) => RouteMarker(
                          trip: lowestExternalCostsTrip,
                          routeMarkerType: RouteMarkerType.lowestExternalCosts,
                        ),
                        anchorPos: AnchorPos.align(AnchorAlign.left),
                      ),*/
                    ],
                  ),
                ],
              );
            } else {
              return FlutterMap(
                options: MapOptions(
                  plugins: [
                    TappablePolylineMapPlugin(),
                  ],
                  center: LatLng(48.1662627, 11.5768211),
                  zoom: 13.0,
                ),
                layers: [
                  TileLayerOptions(
                      urlTemplate:
                          "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                      subdomains: ['a', 'b', 'c']),

                ],
              );
            }
          },
        ),
        Container(
            alignment: Alignment.bottomRight,
            width: double.infinity,
            height: double.infinity,
            child: const Text(
              "© OpenStreetMap",
              style: TextStyle(backgroundColor: Colors.grey, fontSize: 14),
            ))
      ],
    );
  }

  mapSegmentModeToColor(String segmentType) {
    final Values values = Values();

    switch (segmentType) {
      case 'CAR':
        return values.carColor;

      case 'ECAR':
        return values.carColor;

      case 'MOPED':
        return values.mopedColor;

      case 'EMOPED':
        return values.mopedColor;

      case 'BICYCLE':
        return values.bikeColor;

      case 'EBICYCLE':
        return values.bikeColor;

      case 'TIER':
        return values.tierColor;

      case 'EMMY':
        return values.emmyColor;

      case 'FLINKSTER':
        return values.flinksterColor;

      case 'CAB':
        return values.cabColor;

      case 'SHARENOW':
        return values.sharenowColor;

      case 'WALK':
        return values.walkColor;

      case 'METRO':
        return values.metroColor;

      case 'REGIONAL_TRAIN':
        return values.trainColor;

      case 'TRAM':
        return values.tramColor;

      case 'BUS':
        return values.busColor;

      default:
        return values.carColor;
    }
  }
}
