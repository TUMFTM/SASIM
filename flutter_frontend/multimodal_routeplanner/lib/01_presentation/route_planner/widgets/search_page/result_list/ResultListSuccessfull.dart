import 'package:flutter/material.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/search_page/result_list/result_list_item/ResultListItem.dart';
import '../../../../../03_domain/entities/Trip.dart';
import '../result_diagram/ResultDiagramCard.dart';

class ResultList extends StatelessWidget {
  final List<Trip> trips;

  const ResultList({Key? key, required this.trips}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return SingleChildScrollView(
      child: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text('klicke auf ein Ergebnis um die Route anzuzeigen',
                textAlign: TextAlign.center,
                style: TextStyle(
                    fontSize: 14,
                    fontStyle: FontStyle.italic,
                    color: themeData.colorScheme.onPrimary)),
          ),
          //loop over list of trips and return the results

          for (var i = 0; i < trips.length; i++)
            (ResultListItem3(trips: trips, trip: trips[i], index: i)),

          // show a diagram with some date2
          if (trips.isNotEmpty)
            ResultDiagramCard(
              trips: trips,
            ),
        ],
      ),
    );
  }
}

class DiagramData {
  final String dataName;
  final double value;

  DiagramData(this.dataName, this.value);
}
