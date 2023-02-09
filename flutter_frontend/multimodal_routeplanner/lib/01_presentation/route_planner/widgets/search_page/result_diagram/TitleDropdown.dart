import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:multimodal_routeplanner/02_application/bloc/diagram_type_bloc.dart';

import '../../../../../03_domain/enums/DiagramTypeEnum.dart';

class TitleDropdown extends StatelessWidget {
  const TitleDropdown({super.key});

  @override
  Widget build(BuildContext context) {
    final themeData = Theme.of(context);

    return BlocBuilder<DiagramTypeBloc, DiagramTypeState>(
      builder: (context, state) {
        if (state is DiagramTypeSelected) {
          return DropdownButton<DiagramTypeEnum>(
            value: state.type,
            icon: const Icon(Icons.arrow_downward),
            elevation: 16,
            style: TextStyle(color: themeData.colorScheme.onSecondary),
            onChanged: (DiagramTypeEnum? newValue) {
              if (newValue != null) {
                BlocProvider.of<DiagramTypeBloc>(context)
                    .add(DiagramTypeChangedEvent(diagramType: newValue));
              }
            },
            items: <DiagramTypeEnum>[
              DiagramTypeEnum.externalCosts,
              DiagramTypeEnum.climate,
              DiagramTypeEnum.air,
              DiagramTypeEnum.noise,
              DiagramTypeEnum.space,
              DiagramTypeEnum.accidents,
              DiagramTypeEnum.barrier,
              DiagramTypeEnum.congestion,
              DiagramTypeEnum.duration,
              DiagramTypeEnum.distance,
              DiagramTypeEnum.internalCosts,
              DiagramTypeEnum.costs,
            ].map<DropdownMenuItem<DiagramTypeEnum>>((DiagramTypeEnum value) {
              return DropdownMenuItem<DiagramTypeEnum>(
                value: value,
                child: Text(MapDiagramTypeToString(value)),
              );
            }).toList(),
          );
        } else {
          return DropdownButton<DiagramTypeEnum>(
            value: DiagramTypeEnum.externalCosts,
            icon: const Icon(Icons.arrow_downward),
            elevation: 16,
            style: TextStyle(color: themeData.colorScheme.onSecondary),
            onChanged: (DiagramTypeEnum? newValue) {
              if (newValue != null) {
                BlocProvider.of<DiagramTypeBloc>(context)
                    .add(DiagramTypeChangedEvent(diagramType: newValue));
              }
            },
            items: <DiagramTypeEnum>[
              DiagramTypeEnum.externalCosts,
              DiagramTypeEnum.climate,
              DiagramTypeEnum.air,
              DiagramTypeEnum.noise,
              DiagramTypeEnum.space,
              DiagramTypeEnum.accidents,
              DiagramTypeEnum.barrier,
              DiagramTypeEnum.congestion,
              DiagramTypeEnum.duration,
              DiagramTypeEnum.distance,
              DiagramTypeEnum.internalCosts,
              DiagramTypeEnum.costs,
            ].map<DropdownMenuItem<DiagramTypeEnum>>((DiagramTypeEnum value) {
              return DropdownMenuItem<DiagramTypeEnum>(
                value: value,
                child: Text(MapDiagramTypeToString(value)),
              );
            }).toList(),
          );
        }
      },
    );

    /* Padding(
      padding: const EdgeInsets.all(8.0),
      child: Text('Externe Kosten',
          textAlign: TextAlign.center,
          style: TextStyle(
              fontSize: 14,
              fontStyle: FontStyle.italic,
              color: themeData.colorScheme.onSecondary)),
    ); */
  }
}

String MapDiagramTypeToString(DiagramTypeEnum type) {
  switch (type) {
    case DiagramTypeEnum.accidents:
      return 'Unfallkosten';
    case DiagramTypeEnum.air:
      return 'Luftverschmutzung';
    case DiagramTypeEnum.climate:
      return 'Klimaschädigung';
    case DiagramTypeEnum.noise:
      return 'Lärmbelastung';
    case DiagramTypeEnum.space:
      return 'Flächenverbrauch';
    case DiagramTypeEnum.barrier:
      return 'Barriereeffekte';
    case DiagramTypeEnum.congestion:
      return 'Stau';
    case DiagramTypeEnum.externalCosts:
      return 'externe Kosten';
    case DiagramTypeEnum.distance:
      return 'Distanz';
    case DiagramTypeEnum.duration:
      return 'Reisezeit';
    case DiagramTypeEnum.internalCosts:
      return 'interne Kosten';
    case DiagramTypeEnum.costs:
      return 'Gesamtkosten';
    default:
      return '!! kein passendes Label gefunden !!';
  }
}
