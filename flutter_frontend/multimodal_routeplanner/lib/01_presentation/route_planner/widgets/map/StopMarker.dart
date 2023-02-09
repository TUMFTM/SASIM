import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';

class StopMarker extends StatelessWidget {
  const StopMarker({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
        decoration: BoxDecoration(
          color: Colors.red.shade400,
          borderRadius: const BorderRadius.all(
            Radius.circular(20),
          ),
        ),
        height: double.infinity,
        width: double.infinity,
        child: const Center(child: Icon(Icons.location_on_outlined)));
  }
}
