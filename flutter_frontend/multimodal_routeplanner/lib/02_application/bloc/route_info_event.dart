part of 'route_info_bloc.dart';

@immutable
abstract class RouteInfoEvent {}

class ShowRouteInfoEvent extends RouteInfoEvent {
  final Trip trip;

  ShowRouteInfoEvent({required this.trip});
}

class HideRouteInfoEvent extends RouteInfoEvent{
  final Trip trip;

  HideRouteInfoEvent({required this.trip});
}