import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';

class StartMarker extends StatelessWidget {
  const StartMarker({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
        decoration: BoxDecoration(
          color: Colors.green.shade400,
          borderRadius: const BorderRadius.all(
            Radius.circular(20),
          ),
        ),
        height: double.infinity,
        width: double.infinity,
        child: const Center(child: Icon(Icons.directions_walk_outlined)));
  }
}
