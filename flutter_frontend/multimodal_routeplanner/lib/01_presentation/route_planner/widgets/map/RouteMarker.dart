import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import '../../../../03_domain/entities/Trip.dart';
import '../../../../03_domain/enums/RouteMarkerTypeEnum.dart';
import '../../../helpers/ModeMapingHelper.dart';

class RouteMarker extends StatelessWidget {
  final Trip trip;
  final RouteMarkerType routeMarkerType;

  const RouteMarker(
      {super.key, required this.trip, required this.routeMarkerType});

  @override
  Widget build(BuildContext context) {
    ModeMappingHelper stringMappingHelper = ModeMappingHelper();
    return Padding(
      padding: routeMarkerType == RouteMarkerType.fastest
          ? const EdgeInsets.fromLTRB(2, 0, 0, 72)
          : routeMarkerType == RouteMarkerType.lowestExternalCosts
              ? const EdgeInsets.fromLTRB(0, 72, 2, 0)
              : const EdgeInsets.fromLTRB(0, 72, 2, 0),
      child: Container(
        decoration: BoxDecoration(
          color: routeMarkerType == RouteMarkerType.fastest
              ? Colors.blue.shade400
              : routeMarkerType == RouteMarkerType.lowestExternalCosts
                  ? Colors.green.shade400
                  : Colors.blue.shade400,
          borderRadius: const BorderRadius.all(
            Radius.circular(20),
          ),
        ),
        height: double.infinity,
        width: double.infinity,
        child: Row(
          children: [
            Center(
              child: Padding(
                padding: stringMappingHelper
                            .mapModeStringToIcon(trip.mode)
                            .runtimeType ==
                        Icon
                    ? const EdgeInsets.fromLTRB(8, 2.5, 4, 2.5)
                    : const EdgeInsets.fromLTRB(0, 2.5, 4, 2.5),
                child: Container(
                  child: stringMappingHelper
                              .mapModeStringToIcon(trip.mode)
                              .runtimeType ==
                          Icon
                      ? stringMappingHelper.mapModeStringToIcon(trip.mode)
                      : Container(
                          child: stringMappingHelper
                              .mapModeStringToIcon(trip.mode),
                        ),
                ),
              ),
            ),
            Center(
              child: Text(
                routeMarkerType == RouteMarkerType.fastest
                    ? "schnellste"
                    : routeMarkerType == RouteMarkerType.lowestExternalCosts
                        ? "geringste Externe Kosten"
                        : "Markertype unbekannt",
                style: const TextStyle(fontSize: 16),
                textAlign: TextAlign.center,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
