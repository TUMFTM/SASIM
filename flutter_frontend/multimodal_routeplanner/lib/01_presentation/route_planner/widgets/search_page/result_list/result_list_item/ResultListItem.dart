import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:multimodal_routeplanner/01_presentation/helpers/ModeMapingHelper.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/search_page/result_list/result_list_item/RouteIndicator.dart';
import 'package:multimodal_routeplanner/02_application/bloc/route_info_bloc.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';

import '../../../../../../02_application/bloc/visualization_bloc.dart';

class ResultListItem3 extends StatelessWidget {
  final List<Trip> trips;
  final Trip trip;
  final int index;

  const ResultListItem3(
      {Key? key, required this.trips, required this.trip, required this.index})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);
    ModeMappingHelper stringMappingHelper = ModeMappingHelper();

    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 1),
      child: SizedBox(
        width: double.infinity,
        child: InkWell(
          onTap: () {
            BlocProvider.of<VisualizationBloc>(context).add(
                ChangeRouteVizualizationEvent(
                    selectedTrip: trip, trips: trips));
          },
          child: Card(
            color: themeData.colorScheme.onPrimary,
            child: Padding(
              padding: const EdgeInsets.symmetric(vertical: 8.0),
              child: IntrinsicHeight(
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    Expanded(
                      flex: 2,
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          stringMappingHelper
                              .mapModeStringToIcon(trip.mode.toString()),
                        ],
                      ),
                    ),
                    Expanded(
                      flex: 3,
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: [
                          RichText(
                            textAlign: TextAlign.left,
                            text: TextSpan(
                              text: trip.duration.toStringAsFixed(2),
                              style: const TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.black),
                              children: const [
                                TextSpan(
                                  text: " Min",
                                  style: TextStyle(
                                      fontSize: 14,
                                      fontWeight: FontWeight.normal,
                                      color: Colors.black),
                                )
                              ],
                            ),
                          ),
                          RichText(
                            textAlign: TextAlign.left,
                            text: TextSpan(
                              text: (trip.costs.externalCosts.all +
                                      trip.costs.internalCosts.all)
                                  .toStringAsFixed(2),
                              style: const TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold, color: Colors.black),
                              children: const [
                                TextSpan(
                                  text: " €",
                                  style: TextStyle(
                                      fontSize: 14,
                                      fontWeight: FontWeight.normal, color: Colors.black),
                                )
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                    Expanded(
                      flex: 4,
                      child: SizedBox(
                        width: double.infinity,
                        height: 50,
                        child: Image(
                          image: stringMappingHelper
                              .mapMobiScoreStringToPath(trip.mobiScore),
                        ),
                      ),
                    ),
                    Expanded(
                      flex: 1,
                      child: IconButton(
                        onPressed: () {
                          BlocProvider.of<RouteInfoBloc>(context)
                              .add(ShowRouteInfoEvent(trip: trip));
                        },
                        icon: const Icon(Icons.info, color: Colors.grey),
                        hoverColor: Colors.transparent,
                      ),
                    ),
                    Expanded(flex: 1, child: RouteIndicatorWidget(trip: trip)),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
