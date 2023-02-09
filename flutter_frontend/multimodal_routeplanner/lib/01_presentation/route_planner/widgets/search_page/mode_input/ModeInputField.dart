import 'package:flutter/material.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/search_page/mode_input/SelectionIconButton.dart';
import 'package:multimodal_routeplanner/02_application/bloc/route_planner/advanced_route_planner_bloc.dart';
import 'package:multimodal_routeplanner/03_domain/entities/MobilityMode.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';
import 'package:multimodal_routeplanner/03_domain/enums/MobilityModeEnum.dart';

class AdvancedModeInputField extends StatelessWidget {
  final String startAddress;
  final String endAddress;
  final AdvancedRoutePlannerBloc routeBlocProvider;
  final Map<String, Trip> trips;
  final Map<String, Trip> selectedTrips;

  const AdvancedModeInputField({
    Key? key,
    required this.startAddress,
    required this.endAddress,
    required this.routeBlocProvider,
    required this.trips,
    required this.selectedTrips,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(8, 8, 8, 8),
          child: Row(children: [
            Expanded(
                child: Divider(
                    thickness: 3, color: themeData.colorScheme.onPrimary)),
            Padding(
              padding: const EdgeInsets.fromLTRB(8, 0, 8, 0),
              child: Text("individuelle Wege",
                  style: themeData.textTheme.headline1),
            ),
            Expanded(
                child: Divider(
                    thickness: 3, color: themeData.colorScheme.onPrimary)),
          ]),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            AdvancedSelectionIconButton(
              mode: MobilityMode(mode: MobilityModeEnum.walk),
              trips: trips,
              routeBlocProvider: routeBlocProvider,
              startAddress: startAddress,
              endAddress: endAddress,
              selectedTrips: selectedTrips,
            ),
          ],
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.car),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.bike),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.moped),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips)
          ],
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.ecar),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.ebike),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.emoped),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
          ],
        ),
        Padding(
          padding: const EdgeInsets.fromLTRB(8, 8, 8, 8),
          child: Row(children: [
            Expanded(
                child: Divider(
                    thickness: 3, color: themeData.colorScheme.onPrimary)),
            Padding(
              padding: const EdgeInsets.fromLTRB(8, 0, 8, 0),
              child: Text("Wege mit Sharing",
                  style: themeData.textTheme.headline1),
            ),
            Expanded(
                child: Divider(
                    thickness: 3, color: themeData.colorScheme.onPrimary)),
          ]),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [

            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.emmy),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.tier),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),

            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.sharenow),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
          ],
        ),
        Padding(
          padding: const EdgeInsets.fromLTRB(8, 8, 8, 8),
          child: Row(children: [
            Expanded(
                child: Divider(
                    thickness: 3, color: themeData.colorScheme.onPrimary)),
            Padding(
              padding: const EdgeInsets.fromLTRB(8, 0, 8, 0),
              child:
                  Text("Wege mit ÖPNV", style: themeData.textTheme.headline1),
            ),
            Expanded(
                child: Divider(
                    thickness: 3, color: themeData.colorScheme.onPrimary)),
          ]),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.mvg),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
            AdvancedSelectionIconButton(
                mode: MobilityMode(mode: MobilityModeEnum.intermodal),
                trips: trips,
                routeBlocProvider: routeBlocProvider,
                startAddress: startAddress,
                endAddress: endAddress,
                selectedTrips: selectedTrips),
          ],
        ),
      ],
    );
  }
}
