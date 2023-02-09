part of 'diagram_type_bloc.dart';

@immutable
abstract class DiagramTypeState {}

class DiagramTypeInitial extends DiagramTypeState {}

class DiagramTypeExternalCosts extends DiagramTypeState {}

// class DiagramTypeInternalCosts extends DiagramTypeState {}

class DiagramTypeAirCosts extends DiagramTypeState {}

class DiagramTypeNoiseCosts extends DiagramTypeState {}

class DiagramTypeClimateCosts extends DiagramTypeState {}

class DiagramTypeUpstreamCosts extends DiagramTypeState {}

class DiagramTypeAccidentsCosts extends DiagramTypeState {}

class DiagramTypeSpaceCosts extends DiagramTypeState {}

class DiagramTypeDistance extends DiagramTypeState {}

class DiagramTypeDuration extends DiagramTypeState {}

class DiagramTypeSelected extends DiagramTypeState {
  final DiagramTypeEnum type;
  DiagramTypeSelected({required this.type});
}
