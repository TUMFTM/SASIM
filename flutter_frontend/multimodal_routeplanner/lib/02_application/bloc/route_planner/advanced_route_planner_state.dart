part of 'advanced_route_planner_bloc.dart';

@immutable
abstract class AdvancedRoutePlannerState {}

class AdvancedRoutePlannerInitial extends AdvancedRoutePlannerState {}

class LoadingFirstTrip extends AdvancedRoutePlannerState {}

class FirstTripLoaded extends AdvancedRoutePlannerState {

  final String startAddress;
  final String endAddress;
  final Trip trip;

  FirstTripLoaded(this.trip, this.startAddress, this.endAddress);
}

class FistTripError extends AdvancedRoutePlannerState{
  final String message;

  FistTripError({required this.message});
}

class LoadingTrip extends AdvancedRoutePlannerState {}

class TripLoaded extends AdvancedRoutePlannerState {
  final String startAddress;
  final String endAddress;
  final Trip trip;

  TripLoaded(this.trip, this.startAddress, this.endAddress);
}

class TripAddedOrRemoved extends AdvancedRoutePlannerState{
  final Map<String, Trip> trips;

  TripAddedOrRemoved(this.trips);
}

class TripAdded extends AdvancedRoutePlannerState{
  final Map<String, Trip> trips;

  TripAdded(this.trips);
}

class TripRemoved extends AdvancedRoutePlannerState{
  final Map<String, Trip> trips;

  TripRemoved(this.trips);
}

class TripError extends AdvancedRoutePlannerState{
  final String message;

  TripError({required this.message});
}



