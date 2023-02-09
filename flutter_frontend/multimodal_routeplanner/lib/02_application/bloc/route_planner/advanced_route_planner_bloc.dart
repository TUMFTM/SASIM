import 'dart:async';
import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';
import 'package:multimodal_routeplanner/03_domain/entities/MobilityMode.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';
import 'package:multimodal_routeplanner/03_domain/usecases/route_usecases.dart';

part 'advanced_route_planner_event.dart';

part 'advanced_route_planner_state.dart';

class AdvancedRoutePlannerBloc
    extends Bloc<AdvancedRoutePlannerEvent, AdvancedRoutePlannerState> {
  AdvancedRoutePlannerBloc() : super(AdvancedRoutePlannerInitial()) {
    final usecases = RoutePlannerUsecases();

    on<AdvancedRoutePlannerEvent>((event, emit) async {
      if (event is RouteFirstTripEvent) {
        emit(LoadingFirstTrip());

        try {
          final trip = await usecases.getTrip(
              startInput: event.startInput,
              endInput: event.endInput,
              mode: event.mode);

          emit(FirstTripLoaded(trip, event.startInput, event.endInput));
          emit(TripLoaded(trip, event.startInput, event.endInput));
        } catch (e) {
          emit(FistTripError(message: e.toString()));
        }
      } else if (event is RouteTripEvent) {
        emit(LoadingTrip());

        try {
          final trip = await usecases.getTrip(
              startInput: event.startInput,
              endInput: event.endInput,
              mode: event.mode);

          emit(TripLoaded(trip, event.startInput, event.endInput));
        } catch (e) {
          emit(TripError(message: e.toString()));
        }
      } else if (event is ResetTripsEvent) {
        emit(AdvancedRoutePlannerInitial());
      } else if (event is AddTripToListEvent) {
        final Map<String, Trip> trips =
            usecases.getListAddedTrips(trips: event.trips, trip: event.trip);

        emit(TripAddedOrRemoved(trips));
      } else if (event is RemoveTripFromListEvent) {
        final Map<String, Trip> trips =
            usecases.getListRemovedTrips(mode: event.mode, trips: event.trips);

        emit(TripAddedOrRemoved(trips));
      }
    });
  }
}
