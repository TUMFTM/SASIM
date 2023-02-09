part of 'route_info_bloc.dart';

@immutable
abstract class RouteInfoState {}

class RouteInfoInitial extends RouteInfoState {}

class RouteInfoLoadedState extends RouteInfoState {
  final Trip trip;

  RouteInfoLoadedState({required this.trip});
}

class RouteInfoHiddenState extends RouteInfoState {
  final Trip trip;

  RouteInfoHiddenState({required this.trip});
}
