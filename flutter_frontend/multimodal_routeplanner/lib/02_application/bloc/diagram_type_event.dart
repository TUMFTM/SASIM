part of 'diagram_type_bloc.dart';

@immutable
abstract class DiagramTypeEvent {}

class DiagramTypeChangedEvent extends DiagramTypeEvent {
  final DiagramTypeEnum diagramType;
  DiagramTypeChangedEvent({required this.diagramType});
}
