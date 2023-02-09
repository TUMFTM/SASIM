part of 'advanced_route_planner_bloc.dart';

@immutable
abstract class AdvancedRoutePlannerEvent {}

class RouteFirstTripEvent extends AdvancedRoutePlannerEvent {
  final String startInput;
  final String endInput;
  final MobilityMode mode;

  RouteFirstTripEvent(this.startInput, this.endInput, this.mode);

}

class RouteTripEvent extends AdvancedRoutePlannerEvent{
  final String startInput;
  final String endInput;
  final MobilityMode mode;

  RouteTripEvent(this.startInput, this.endInput, this.mode);
}

class ResetTripsEvent extends AdvancedRoutePlannerEvent{}

class RemoveTripFromListEvent extends AdvancedRoutePlannerEvent{
  final String mode;
  final Map<String, Trip> trips;

  RemoveTripFromListEvent(this.mode, this.trips);
}

class AddTripToListEvent extends AdvancedRoutePlannerEvent{
  final Trip trip;
  final Map<String, Trip> trips;

  AddTripToListEvent(this.trip, this.trips);
}