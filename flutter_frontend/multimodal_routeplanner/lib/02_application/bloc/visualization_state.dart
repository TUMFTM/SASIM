part of 'visualization_bloc.dart';

@immutable
abstract class VisualizationState {}

class VisualizationInitial extends VisualizationState {}

class VizualizationLoadedState extends VisualizationState {}

class VisualizationChangedState extends VisualizationState {
  final Trip fastestTrip;
  final Trip lowestExternalCostsTrip;
  final Trip selectedTrip;

  VisualizationChangedState(
      {required this.fastestTrip,
      required this.lowestExternalCostsTrip,
      required this.selectedTrip});
}

class VisualizationRemovedState extends VisualizationState{}
