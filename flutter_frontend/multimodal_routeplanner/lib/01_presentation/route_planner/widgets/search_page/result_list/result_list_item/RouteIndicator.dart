import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../../../../../02_application/bloc/visualization_bloc.dart';
import '../../../../../../03_domain/entities/Trip.dart';

class RouteIndicatorWidget extends StatelessWidget {
  final Trip trip;
  const RouteIndicatorWidget({super.key, required this.trip});

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);
    bool isSelected = false;
    return BlocBuilder<VisualizationBloc, VisualizationState>(
        builder: (context, routePlannerState) {
      if (routePlannerState is VisualizationChangedState) {
        if (routePlannerState.selectedTrip == trip) {
          isSelected = true;
        } else {
          isSelected = false;
        }
      }
      return VerticalDivider(
        thickness: 3,
        color:
            isSelected ? themeData.colorScheme.secondary : Colors.grey.shade300,
        indent: 0,
      );
    });
  }
}
