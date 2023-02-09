import 'package:bloc/bloc.dart';
import 'package:meta/meta.dart';

import '../../03_domain/enums/DiagramTypeEnum.dart';

part 'diagram_type_event.dart';
part 'diagram_type_state.dart';

class DiagramTypeBloc extends Bloc<DiagramTypeEvent, DiagramTypeState> {
  DiagramTypeBloc() : super(DiagramTypeInitial()) {
    on<DiagramTypeEvent>((event, emit) {
      if (event is DiagramTypeChangedEvent) {
        emit(DiagramTypeSelected(type: event.diagramType));
      }
    });
  }
}
