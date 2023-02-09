part of 'cost_details_bloc.dart';

@immutable
abstract class CostDetailsEvent {}

class ShowCostDetailsEvent extends CostDetailsEvent {
  final Costs costs;
  ShowCostDetailsEvent({required this.costs});
}

class HideCostDetailsEvent extends CostDetailsEvent {}
