import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:multimodal_routeplanner/01_presentation/helpers/ModeMapingHelper.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/route_info/ExternalCostsDetailRow.dart';
import 'package:multimodal_routeplanner/02_application/bloc/route_info_bloc.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';

class RouteInfo extends StatelessWidget {
  final Trip trip;
  final bool visible;

  const RouteInfo({Key? key, required this.trip, required this.visible})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);
    ModeMappingHelper stringMappingHelper = ModeMappingHelper();

    return Visibility(
      visible: visible,
      child: Align(
        alignment: Alignment.center,
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              SizedBox(
                width: 300,
                child: Card(
                  color: themeData.colorScheme.onPrimary,
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Stack(
                      children: [
                        Column(
                          mainAxisAlignment: MainAxisAlignment.start,
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            //Header Row 1
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Padding(
                                  padding: const EdgeInsets.all(8.0),
                                  child: stringMappingHelper
                                      .mapModeStringToIcon(trip.mode.toString()),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(8.0),
                                  child: Text(
                                      stringMappingHelper
                                          .mapModeStringToToolTip(trip.mode),
                                      style: const TextStyle(
                                          fontWeight: FontWeight.bold)),
                                ),
                              ],
                            ),
                            const SizedBox(
                              height: 4,
                            ),
                            // Header Row 2
                            Row(
                                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                children: [
                                  Column(
                                    children: [
                                      Row(children: [
                                        const Icon(Icons.timer),
                                        Text(
                                            '${trip.duration.toStringAsFixed(2)} min')
                                      ])
                                    ],
                                  ),
                                  Column(children: [
                                    Row(
                                      children: [
                                        const Icon(Icons.route),
                                        Text(
                                            '${trip.distance.toStringAsFixed(2)} km')
                                      ],
                                    ),
                                  ]),
                                ]),
                            const Divider(
                              thickness: 1,
                            ),
                            // MobiScore information
                            ExpansionTile(
                              title: Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  const Text('MobiScore '),
                                  SizedBox(
                                    width: 100,
                                    height: 50,
                                    child: Image(
                                      image: stringMappingHelper
                                          .mapMobiScoreStringToPath(
                                              trip.mobiScore),
                                    ),
                                  ),
                                ],
                              ),
                              subtitle: const Text(
                                'erfahre mehr zum MobiScore',
                                style: TextStyle(fontSize: 12),
                                textAlign: TextAlign.right,
                              ),
                              children: [
                                Column(
                                  children: const [
                                    SizedBox(height: 8),
                                    Text(
                                      'Der MobiScore ist eine Kenngröße, die die Nachhaltigkeit einer Route im urbanen Verkehr beschreibt. Diese wird aus den externen Kosten und der Routendistanz berechnet.',
                                      textAlign: TextAlign.justify,
                                      textWidthBasis: TextWidthBasis.parent,
                                      style: TextStyle(fontSize: 14),
                                    ),
                                    SizedBox(height: 8),
                                  ],
                                ),
                              ],
                            ),
                            const Divider(
                              thickness: 1,
                            ),
                            // Costs information
                            ExpansionTile(
                              title: Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  const Text('Kosten'),
                                  Column(
                                    children: [
                                      Text(
                                          'intern: ${trip.costs.internalCosts.all.toStringAsFixed(2)} €'),
                                      Text(
                                          'extern: ${trip.costs.externalCosts.all.toStringAsFixed(2)} €')
                                    ],
                                  )
                                ],
                              ),
                              subtitle: const Text(
                                'erfahre mehr zu den Kosten',
                                style: TextStyle(fontSize: 12),
                                textAlign: TextAlign.right,
                              ),
                              children: [
                                Column(
                                  children: [
                                    Padding(
                                      padding: const EdgeInsets.all(4),
                                      child: Text(
                                        'Bei dieser Fahrt entstehen ${trip.costs.internalCosts.all.toStringAsFixed(2)}€ interne Kosten und ${trip.costs.externalCosts.all.toStringAsFixed(2)}€ externe Kosten. Die externen Kosten setzen sich dabei folgendermaßen zusammen:',
                                        textAlign: TextAlign.justify,
                                        style: const TextStyle(fontSize: 14),
                                      ),
                                    ),
                                    const SizedBox(height: 4),
                                    ExternalCostsDetailRow(
                                        externalCostName: 'Unfallkosten',
                                        externalCostValue:
                                            trip.costs.externalCosts.accidents,
                                        costIcon: Icons.emergency),
                                    ExternalCostsDetailRow(
                                        externalCostName: 'Klimaschäden',
                                        externalCostValue:
                                            trip.costs.externalCosts.climate,
                                        costIcon: Icons.eco),
                                    ExternalCostsDetailRow(
                                        externalCostName: 'Luftverschmutzung',
                                        externalCostValue:
                                            trip.costs.externalCosts.air,
                                        costIcon: Icons.air),
                                    ExternalCostsDetailRow(
                                        externalCostName: 'Lärmbelastung',
                                        externalCostValue:
                                            trip.costs.externalCosts.noise,
                                        costIcon: Icons.volume_up),
                                    ExternalCostsDetailRow(
                                        externalCostName: 'Fächenverbrauch',
                                        externalCostValue:
                                            trip.costs.externalCosts.space,
                                        costIcon: Icons.location_city),
                                    ExternalCostsDetailRow(
                                        externalCostName: 'Stau',
                                        externalCostValue:
                                            trip.costs.externalCosts.congestion,
                                        costIcon: Icons.traffic),
                                    ExternalCostsDetailRow(
                                        externalCostName: 'Barriereeffekte',
                                        externalCostValue:
                                            trip.costs.externalCosts.barrier,
                                        costIcon: Icons.fence),
                                    const SizedBox(height: 8),
                                  ],
                                )
                              ],
                            )
                          ],
                        ),
                        Align(
                            alignment: Alignment.topRight,
                            child: IconButton(
                                onPressed: () {
                                  BlocProvider.of<RouteInfoBloc>(context)
                                      .add(HideRouteInfoEvent(trip: trip));
                                },
                                icon: const Icon(Icons.close))),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
