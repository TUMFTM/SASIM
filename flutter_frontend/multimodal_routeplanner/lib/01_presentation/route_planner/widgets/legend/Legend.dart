import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:multimodal_routeplanner/01_presentation/route_planner/widgets/legend/LegendRow.dart';

import '../../../../values.dart';

class Legend extends StatelessWidget {
  const Legend({super.key});

  @override
  Widget build(BuildContext context) {
    final values = Values();
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.all(Radius.circular(5)),
            color: Colors.grey.withOpacity(0.8),
          ),
          child: Wrap(
            direction: Axis.vertical,
            children: [
              LegendRow(modeString: "zu Fuß", color: values.walkColor),
              LegendRow(
                modeString: "Fahrrad",
                color: values.bikeColor,
              ),
              LegendRow(
                modeString: "U-Bahn",
                color: values.metroColor,
              ),
              LegendRow(
                modeString: "Bus",
                color: values.busColor,
              ),
              LegendRow(
                modeString: "Tram",
                color: values.tramColor,
              ),
              LegendRow(
                modeString: "S-Bahn",
                color: values.trainColor,
              ),
            ],
          )),
    );
  }
}
