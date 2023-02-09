import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import '../../../../../02_application/bloc/cost_details_bloc.dart';
import '../../../../../03_domain/entities/Costs/Costs.dart';

class CostDetails extends StatelessWidget {
  final Costs costs;

  const CostDetails({super.key, required this.costs});

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Row(
        children: [
          IconButton(
              onPressed: () {
                BlocProvider.of<CostDetailsBloc>(context)
                    .add(HideCostDetailsEvent());
              },
              icon: const Icon(Icons.close)),
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text('Luftverschmutzung: ',
                  textAlign: TextAlign.right,
                  style: TextStyle(
                      fontSize: 12,
                      fontStyle: FontStyle.normal,
                      fontWeight: FontWeight.bold,
                      color: themeData.colorScheme.onSecondary)),
              Text('Klimaschäden: ',
                  textAlign: TextAlign.right,
                  style: TextStyle(
                      fontSize: 12,
                      fontStyle: FontStyle.normal,
                      fontWeight: FontWeight.bold,
                      color: themeData.colorScheme.onSecondary)),
              Text('Lärm: ',
                  textAlign: TextAlign.right,
                  style: TextStyle(
                      fontSize: 12,
                      fontStyle: FontStyle.normal,
                      fontWeight: FontWeight.bold,
                      color: themeData.colorScheme.onSecondary)),
              Text('Flächenverbrauch: ',
                  textAlign: TextAlign.right,
                  style: TextStyle(
                      fontSize: 12,
                      fontStyle: FontStyle.normal,
                      fontWeight: FontWeight.bold,
                      color: themeData.colorScheme.onSecondary)),
              Text('Barriereeffekte: ',
                  textAlign: TextAlign.right,
                  style: TextStyle(
                      fontSize: 12,
                      fontStyle: FontStyle.normal,
                      fontWeight: FontWeight.bold,
                      color: themeData.colorScheme.onSecondary)),
              Text('Unfälle: ',
                  textAlign: TextAlign.right,
                  style: TextStyle(
                      fontSize: 12,
                      fontStyle: FontStyle.normal,
                      fontWeight: FontWeight.bold,
                      color: themeData.colorScheme.onSecondary)),
              Text('Stau: ',
                  textAlign: TextAlign.right,
                  style: TextStyle(
                      fontSize: 12,
                      fontStyle: FontStyle.normal,
                      fontWeight: FontWeight.bold,
                      color: themeData.colorScheme.onSecondary)),
            ],
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(4, 0, 0, 0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('${costs.externalCosts.air.toStringAsFixed(2)} €',
                    textAlign: TextAlign.left,
                    style: TextStyle(
                        fontSize: 12,
                        fontStyle: FontStyle.normal,
                        fontWeight: FontWeight.bold,
                        color: themeData.colorScheme.onSecondary)),
                Text('${costs.externalCosts.climate.toStringAsFixed(2)} €',
                    textAlign: TextAlign.left,
                    style: TextStyle(
                        fontSize: 12,
                        fontStyle: FontStyle.normal,
                        fontWeight: FontWeight.bold,
                        color: themeData.colorScheme.onSecondary)),
                Text('${costs.externalCosts.noise.toStringAsFixed(2)} €',
                    textAlign: TextAlign.left,
                    style: TextStyle(
                        fontSize: 12,
                        fontStyle: FontStyle.normal,
                        fontWeight: FontWeight.bold,
                        color: themeData.colorScheme.onSecondary)),
                Text('${costs.externalCosts.space.toStringAsFixed(2)} €',
                    textAlign: TextAlign.left,
                    style: TextStyle(
                        fontSize: 12,
                        fontStyle: FontStyle.normal,
                        fontWeight: FontWeight.bold,
                        color: themeData.colorScheme.onSecondary)),
                Text('${costs.externalCosts.barrier.toStringAsFixed(2)} €',
                    textAlign: TextAlign.left,
                    style: TextStyle(
                        fontSize: 12,
                        fontStyle: FontStyle.normal,
                        fontWeight: FontWeight.bold,
                        color: themeData.colorScheme.onSecondary)),
                Text('${costs.externalCosts.accidents.toStringAsFixed(2)} €',
                    textAlign: TextAlign.left,
                    style: TextStyle(
                        fontSize: 12,
                        fontStyle: FontStyle.normal,
                        fontWeight: FontWeight.bold,
                        color: themeData.colorScheme.onSecondary)),
                Text('${costs.externalCosts.congestion.toStringAsFixed(2)} €',
                    textAlign: TextAlign.left,
                    style: TextStyle(
                        fontSize: 12,
                        fontStyle: FontStyle.normal,
                        fontWeight: FontWeight.bold,
                        color: themeData.colorScheme.onSecondary)),
              ],
            ),
          )
        ],
      ),
    );
  }
}
