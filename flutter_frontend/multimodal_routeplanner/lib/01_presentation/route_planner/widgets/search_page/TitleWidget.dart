import 'package:flutter/material.dart';

class TitleWidget extends StatelessWidget {
  const TitleWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'SASIM',
            textAlign: TextAlign.start,
            style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 30,
                color: themeData.colorScheme.onPrimary),
          ),
          Text(
            'Smart Advisor for Sustainable Integrated Mobility',
            textAlign: TextAlign.start,
            style: TextStyle(
                fontSize: 14, color: themeData.colorScheme.onPrimary),
          ),
          Text(
            'Eine Vollkostenperspektive auf den urbanen Verkehr',
            textAlign: TextAlign.start,
            style: TextStyle(
                fontSize: 14, color: themeData.colorScheme.onPrimary),
          ),
        ],
      ),
    );
  }
}
