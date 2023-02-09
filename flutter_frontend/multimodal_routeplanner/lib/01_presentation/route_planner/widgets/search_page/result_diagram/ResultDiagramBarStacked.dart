/// Bar chart example
import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/search_page/result_diagram/DiagramHelper.dart';
import 'package:multimodal_routeplanner/03_domain/enums/DiagramTypeEnum.dart';

import '../../../../../03_domain/entities/Trip.dart';

class ResultDiagramBarStackedWidget extends StatelessWidget {
  final List<Trip> trips;
  final bool animate;
  final DiagramTypeEnum diagramType;

  final DiagramHelper diagramHelper = DiagramHelper();

  ResultDiagramBarStackedWidget(
      {Key? key,
      required this.trips,
      this.animate = false,
      required this.diagramType})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return charts.BarChart(
      diagramHelper.createDiagramDataBarStacked(trips: trips),
      animate: animate,
      barGroupingType: charts.BarGroupingType.stacked,
      defaultInteractions: true,
    );
  }

  // methods for diagram data

}
