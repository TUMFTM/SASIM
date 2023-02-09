part of 'route_planner_bloc.dart';

@immutable
abstract class RoutePlannerState {}

class RoutePlannerInitial extends RoutePlannerState {}

class RoutePlannerStateLoading extends RoutePlannerState {}

class RoutePlannerStateLoaded extends RoutePlannerState {
  final Map<String, Trip> trips;
  RoutePlannerStateLoaded({required this.trips});
}

class RoutePlannerStateError extends RoutePlannerState {
  final String message;

  RoutePlannerStateError({required this.message});
}

class RouteVisualizationStateChanged extends RoutePlannerState {
  final Trip selectedTrip;

  RouteVisualizationStateChanged({required this.selectedTrip});
}
