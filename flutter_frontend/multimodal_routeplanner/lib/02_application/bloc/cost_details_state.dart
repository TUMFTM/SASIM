part of 'cost_details_bloc.dart';

@immutable
abstract class CostDetailsState {}

class CostDetailsInitial extends CostDetailsState {}

class CostDetailsLoadedState extends CostDetailsState {
  final Costs costs;
  CostDetailsLoadedState({required this.costs});
}

class CostDetailsHiddenState extends CostDetailsState {}
