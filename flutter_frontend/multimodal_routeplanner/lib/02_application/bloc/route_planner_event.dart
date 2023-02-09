part of 'route_planner_bloc.dart';

@immutable
abstract class RoutePlannerEvent {}

/// event when mobility mode is selected
class RouteRequestedEvent extends RoutePlannerEvent {
  final String startInput;
  final String endInput;
  final MobilityMode mode;
  final Map<String, Trip> trips;

  RouteRequestedEvent(this.startInput, this.endInput, this.mode, this.trips);
}

class DeleteRouteEvent extends RoutePlannerEvent {
  final String mode;
  final Map<String, Trip> trips;

  DeleteRouteEvent(this.mode, this.trips);
}

class VisualizeDifferentRouteEvent extends RoutePlannerEvent {
  final Trip selectedTrip;

  VisualizeDifferentRouteEvent(this.selectedTrip);
}
