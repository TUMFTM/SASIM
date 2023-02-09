import 'package:flutter/material.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/search_page/mode_input/RouteButton.dart';
import 'package:multimodal_routeplanner/02_application/bloc/route_planner/advanced_route_planner_bloc.dart';
import 'package:multimodal_routeplanner/03_domain/entities/MobilityMode.dart';
import 'package:multimodal_routeplanner/03_domain/enums/MobilityModeEnum.dart';

class AdvancedSearchInput extends StatelessWidget {
  final AdvancedRoutePlannerBloc routeBlocProvider;

  const AdvancedSearchInput({Key? key, required this.routeBlocProvider})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    // TODO: remove this when online
    String startAddress = "Arcisstraße 21, München";
    String endAddress = "Schleißheimerstr. 318, München";

    return Column(mainAxisSize: MainAxisSize.min, children: [
      Padding(
        padding: const EdgeInsets.fromLTRB(8, 8, 8, 4),
        child: TextFormField(
          onChanged: ((value) {
            startAddress = value.toString();
          }),
          decoration: const InputDecoration(
            border: OutlineInputBorder(),
            hintText: "Startadresse in München",
            fillColor: Colors.white,
            filled: true,
          ),
        ),
      ),
      Padding(
        padding: const EdgeInsets.fromLTRB(8, 4, 8, 4),
        child: TextFormField(
          onChanged: ((value) {
            endAddress = value.toString();
          }),
          decoration: const InputDecoration(
              border: OutlineInputBorder(),
              hintText: "Zieladresse in München",
              fillColor: Colors.white,
              filled: true),
        ),
      ),
      AdvancedRouteButtonWidget(
        loadFirstTrip: () {
          routeBlocProvider.add(RouteFirstTripEvent(startAddress, endAddress,
              MobilityMode(mode: MobilityModeEnum.mvg)));
        },
      ),
    ]);
  }
}
