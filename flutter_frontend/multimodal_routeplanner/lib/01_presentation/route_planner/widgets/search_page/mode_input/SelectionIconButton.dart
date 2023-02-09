import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:multimodal_routeplanner/01_presentation/helpers/ModeMapingHelper.dart';
import 'package:multimodal_routeplanner/02_application/bloc/route_planner/advanced_route_planner_bloc.dart';
import 'package:multimodal_routeplanner/03_domain/entities/MobilityMode.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';

class AdvancedSelectionIconButton extends StatelessWidget {
  final MobilityMode mode;
  final Map<String, Trip> trips;
  final Map<String, Trip> selectedTrips;
  final AdvancedRoutePlannerBloc routeBlocProvider;
  final String startAddress;
  final String endAddress;

  const AdvancedSelectionIconButton(
      {Key? key,
      required this.trips,
      required this.routeBlocProvider,
      required this.startAddress,
      required this.endAddress,
      required this.selectedTrips,
      required this.mode})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    bool isSelected = false;
    ModeMappingHelper modeMappingHelper = ModeMappingHelper();
    String stringMode = modeMappingHelper.mapModeToStringMode(mode);

    final themeData = Theme.of(context);

    return BlocBuilder<AdvancedRoutePlannerBloc, AdvancedRoutePlannerState>(
      builder: (context, state) {
        {
          if (state is TripAddedOrRemoved) {
            isSelected =
                state.trips[modeMappingHelper.mapModeToStringMode(mode)] !=
                    null;
          }

          return IntrinsicWidth(
            child: SizedBox(
              width: 60,
              child: Column(children: [
                IconButton(
                    onPressed: () {
                      if (trips[stringMode] == null) {
                        routeBlocProvider.add(
                            RouteTripEvent(startAddress, endAddress, mode));
                      } else {
                        if (isSelected) {
                          routeBlocProvider.add(RemoveTripFromListEvent(
                              stringMode, selectedTrips));
                        } else {
                          if (trips[stringMode] != null) {
                            routeBlocProvider.add(AddTripToListEvent(
                                trips[stringMode]!, selectedTrips));
                          }
                        }
                      }
                    },
                    icon: modeMappingHelper
                                .mapModeStringToIcon(stringMode)
                                .runtimeType ==
                            Icon
                        ? modeMappingHelper.mapModeStringToIcon(stringMode)
                        : Container(
                            foregroundDecoration: BoxDecoration(
                                color: isSelected
                                    ? Colors.transparent
                                    : Colors.grey,
                                backgroundBlendMode: isSelected
                                    ? BlendMode.color
                                    : BlendMode.saturation,
                                shape: BoxShape.circle),
                            child: modeMappingHelper
                                .mapModeStringToIcon(stringMode),
                          ),
                    iconSize: modeMappingHelper
                                .mapModeStringToIcon(stringMode)
                                .runtimeType ==
                            Icon
                        ? 25
                        : 40,
                    tooltip:
                        modeMappingHelper.mapModeStringToToolTip(stringMode),
                    color: isSelected
                        ? themeData.colorScheme.secondary
                        : Colors.white),
                Divider(
                  height: 4,
                  thickness: 3,
                  color: isSelected
                      ? themeData.colorScheme.secondary
                      : Colors.grey,
                  indent: 16,
                  endIndent: 16,
                )
              ]),
            ),
          );
        }
      },
    );
  }
}
