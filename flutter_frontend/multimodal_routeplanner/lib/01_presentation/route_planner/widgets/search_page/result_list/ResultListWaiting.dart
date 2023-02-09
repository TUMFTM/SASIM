import 'package:flutter/material.dart';

class ResultListWaiting extends StatelessWidget {
  const ResultListWaiting({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Center(
        child:
            CircularProgressIndicator(color: themeData.colorScheme.secondary),
      ),
    );
  }
}
