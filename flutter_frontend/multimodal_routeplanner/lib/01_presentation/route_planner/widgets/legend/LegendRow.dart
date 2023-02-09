import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:multimodal_routeplanner/values.dart';

class LegendRow extends StatelessWidget {
  final String modeString;
  final Color color;
  const LegendRow({super.key, required this.modeString, required this.color});

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);
    return Padding(
      padding: const EdgeInsets.all(4.0),
      child: Container(
        width: 120,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Expanded(
              flex: 2,
              child: Divider(thickness: 3, color: color),
            ),
            Expanded(
              flex: 7,
              child: Padding(
                padding: const EdgeInsets.fromLTRB(8, 0, 8, 0),
                child: Text(modeString, style: themeData.textTheme.bodyText1),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
