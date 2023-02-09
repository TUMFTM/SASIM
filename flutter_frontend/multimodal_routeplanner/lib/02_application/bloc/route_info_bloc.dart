import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';

part 'route_info_event.dart';
part 'route_info_state.dart';

class RouteInfoBloc extends Bloc<RouteInfoEvent, RouteInfoState> {
  RouteInfoBloc() : super(RouteInfoInitial()) {
    on<RouteInfoEvent>((event, emit) {

      if (event is ShowRouteInfoEvent){
        emit(RouteInfoLoadedState(trip: event.trip));
      }

      if (event is HideRouteInfoEvent){
        emit(RouteInfoHiddenState(trip: event.trip));
      }

    });
  }
}
