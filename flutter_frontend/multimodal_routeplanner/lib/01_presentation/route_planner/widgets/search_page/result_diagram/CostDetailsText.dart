import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';

class CostDetailsText extends StatelessWidget {
  const CostDetailsText({super.key});

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Text(
          'drücke auf das Diagramm, um Details zu den Kosten anzuzeigen',
          textAlign: TextAlign.center,
          style: TextStyle(
              fontSize: 10,
              fontStyle: FontStyle.italic,
              color: themeData.colorScheme.onSecondary)),
    );
  }
}
