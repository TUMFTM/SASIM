import 'package:flutter/material.dart';

class ResetRouteButton extends StatelessWidget {
  final Function resetTrips;

  const ResetRouteButton({super.key, required this.resetTrips});

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Row(
      mainAxisAlignment: MainAxisAlignment.end,
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: InkWell(
            onTap: () {
              resetTrips();
            },
            child: Container(
              width: 200,
              height: 40,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(10),
                color: themeData.colorScheme.secondary,
              ),
              child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Text(
                      'neue Routenplanung starten',
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
