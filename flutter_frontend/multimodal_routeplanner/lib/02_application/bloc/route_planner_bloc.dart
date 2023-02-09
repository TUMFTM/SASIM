import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';
import 'package:multimodal_routeplanner/03_domain/entities/MobilityMode.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';
import 'package:multimodal_routeplanner/03_domain/usecases/route_usecases.dart';

part 'route_planner_event.dart';

part 'route_planner_state.dart';

class RoutePlannerBloc extends Bloc<RoutePlannerEvent, RoutePlannerState> {
  RoutePlannerBloc() : super(RoutePlannerInitial()) {
    final usecases = RoutePlannerUsecases();

    on<RoutePlannerEvent>(
      (event, emit) async {
        if (event is RouteRequestedEvent) {
          emit(RoutePlannerStateLoading());

          // get route result
          try {
            final trip = await usecases.getTrip(
                startInput: event.startInput,
                endInput: event.endInput,
                mode: event.mode);

            final Map<String, Trip> trips =
                usecases.getListAddedTrips(trips: event.trips, trip: trip);

            emit(RoutePlannerStateLoaded(trips: trips));
          } catch (e) {
            emit(RoutePlannerStateError(message: e.toString()));
          }
        }

        if (event is DeleteRouteEvent) {
          emit(RoutePlannerStateLoading());

          final Map<String, Trip> trips = usecases.getListRemovedTrips(
              trips: event.trips, mode: event.mode);

          /* tripOrFailure.fold(
            (failure) => emit(
                RoutePlannerStateError(message: _mapFailureToMessage(failure))),
            (trip) => emit(RoutePlannerStateLoaded(trip: trip))); */
          emit(RoutePlannerStateLoaded(trips: trips));
        }

        if (event is VisualizeDifferentRouteEvent) {
          emit(
            RouteVisualizationStateChanged(selectedTrip: event.selectedTrip),
          );
        }
      },
    );
  }
}
