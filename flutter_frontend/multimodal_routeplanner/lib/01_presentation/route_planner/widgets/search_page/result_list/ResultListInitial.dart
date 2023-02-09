import 'package:flutter/material.dart';

class ResultListInitial extends StatelessWidget {
  const ResultListInitial({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Text("wähle eine Option aus, um eine Route zu planen",
          style: themeData.textTheme.bodyText1),
    );
  }
}
