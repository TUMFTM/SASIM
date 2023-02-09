import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';
import 'package:multimodal_routeplanner/03_domain/usecases/visualization_usecases.dart';

import '../../03_domain/entities/Trip.dart';

part 'visualization_event.dart';
part 'visualization_state.dart';

class VisualizationBloc extends Bloc<VisualizationEvent, VisualizationState> {
  VisualizationBloc() : super(VisualizationInitial()) {
    final usecases = VisualizationUsecases();
    on<VisualizationEvent>(
      (event, emit) {
        if (event is ChangeRouteVizualizationEvent) {
          Trip fastestTrip = usecases.getFastestTrip(trips: event.trips);
          Trip lowestExternalCostsTrip =
              usecases.getLowestExternalCostsTrip(trips: event.trips);

          emit(VisualizationChangedState(
              selectedTrip: event.selectedTrip,
              fastestTrip: fastestTrip,
              lowestExternalCostsTrip: lowestExternalCostsTrip));
        }
        if (event is RemoveRouteVizualizationEvent){
          emit(VisualizationRemovedState());
        }
      },
    );
  }
}
