import 'package:flutter/material.dart';

class ExternalCostsDetailRow extends StatelessWidget {
  final String externalCostName;
  final double externalCostValue;
  final IconData costIcon;

  const ExternalCostsDetailRow(
      {Key? key,
      required this.externalCostName,
      required this.externalCostValue,
      required this.costIcon})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(1),
      child: Row(children: [
        Expanded(
          flex: 5,
          child: Text(
            externalCostName,
            textAlign: TextAlign.right,
            style: const TextStyle(fontSize: 14),
          ),
        ),
        Expanded(
          flex: 2,
          child: Icon(costIcon, size: 18),
        ),
        Expanded(
          flex: 2,
          child: Text(
            '${externalCostValue.toStringAsFixed(2)}€',
            textAlign: TextAlign.left,
            style: const TextStyle(fontSize: 14),
          ),
        )
      ]),
    );
  }
}
