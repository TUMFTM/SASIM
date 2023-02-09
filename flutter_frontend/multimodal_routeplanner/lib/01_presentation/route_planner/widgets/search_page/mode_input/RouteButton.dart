import 'package:flutter/material.dart';

class AdvancedRouteButtonWidget extends StatelessWidget {

  final Function() loadFirstTrip;

  const AdvancedRouteButtonWidget(
      {super.key,
      required this.loadFirstTrip,
      });

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Row(
      mainAxisAlignment: MainAxisAlignment.end,
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: InkWell(
            onTap: () => loadFirstTrip(),
            child: Container(
              width: 120,
              height: 40,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                color: themeData.colorScheme.secondary,
              ),
              child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Text(
                      'neue Route',
                      style: themeData.textTheme.bodySmall,
                    ),
                    const Icon(Icons.directions),
                  ]),
            ),
          ),
        ),
      ],
    );
  }
}
