import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';

import '../../03_domain/entities/Costs/Costs.dart';

part 'cost_details_event.dart';
part 'cost_details_state.dart';

class CostDetailsBloc extends Bloc<CostDetailsEvent, CostDetailsState> {
  CostDetailsBloc() : super(CostDetailsInitial()) {
    on<CostDetailsEvent>((event, emit) {
      if (event is ShowCostDetailsEvent) {
        emit(CostDetailsLoadedState(costs: event.costs));
      }

      if (event is HideCostDetailsEvent) {
        emit(CostDetailsHiddenState());
      }
    });
  }
}
