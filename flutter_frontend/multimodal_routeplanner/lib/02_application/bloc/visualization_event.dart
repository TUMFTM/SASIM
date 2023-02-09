part of 'visualization_bloc.dart';

@immutable
abstract class VisualizationEvent {}

class ChangeRouteVizualizationEvent extends VisualizationEvent {
  final Trip selectedTrip;
  final List<Trip> trips;
  ChangeRouteVizualizationEvent(
      {required this.selectedTrip, required this.trips});
}

class RemoveRouteVizualizationEvent extends VisualizationEvent {}
