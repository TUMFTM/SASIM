import 'package:charts_flutter/flutter.dart' as charts;
import 'package:multimodal_routeplanner/01_presentation/helpers/ModeMapingHelper.dart';

import '../../../../../03_domain/entities/Trip.dart';
import '../../../../../03_domain/enums/DiagramTypeEnum.dart';

class DiagramHelper {
  List<charts.Series<DiagramData, String>> createDiagramDataBarStacked(
      {required List<Trip> trips}) {
    List<charts.Series<DiagramData, String>> results = [];

    List<DiagramData> airData = [];
    List<DiagramData> noiseData = [];
    List<DiagramData> climateData = [];
    List<DiagramData> accidentsData = [];
    List<DiagramData> spaceData = [];
    List<DiagramData> barrierData = [];
    List<DiagramData> congestionData = [];

    // this is WRONG! need different Lists for airData (Car) and airData (Bike))
    for (var i = 0; i < trips.length; i++) {
      airData.add(DiagramData(trips[i].mode, trips[i].costs.externalCosts.air));
      noiseData
          .add(DiagramData(trips[i].mode, trips[i].costs.externalCosts.noise));
      climateData.add(
          DiagramData(trips[i].mode, trips[i].costs.externalCosts.climate));
      accidentsData.add(
          DiagramData(trips[i].mode, trips[i].costs.externalCosts.accidents));
      spaceData
          .add(DiagramData(trips[i].mode, trips[i].costs.externalCosts.space));
      barrierData.add(
          DiagramData(trips[i].mode, trips[i].costs.externalCosts.barrier));
      congestionData.add(
          DiagramData(trips[i].mode, trips[i].costs.externalCosts.congestion));
    }

    results.add(charts.Series<DiagramData, String>(
        id: 'air',
        colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: airData));

    results.add(charts.Series<DiagramData, String>(
        id: 'noise',
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: noiseData));

    results.add(charts.Series<DiagramData, String>(
        id: 'climate',
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: climateData));

    results.add(charts.Series<DiagramData, String>(
        id: 'accidents',
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: accidentsData));

    results.add(charts.Series<DiagramData, String>(
        id: 'space',
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: spaceData));

    results.add(charts.Series<DiagramData, String>(
        id: 'barrier',
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: barrierData));

    results.add(charts.Series<DiagramData, String>(
        id: 'congestion',
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: congestionData));

    // for each loop create a externalCostsData for the mode of i and all external cost types

    return results;
  }

  List<charts.Series<DiagramData, String>> createDiagramDataBar(
      {required List<Trip> trips, required DiagramTypeEnum diagramType}) {
    List<charts.Series<DiagramData, String>> results = [];
    List<DiagramData> data = [];
    final ModeMappingHelper stringMappingHelper = ModeMappingHelper();

    for (var i = 0; i < trips.length; i++) {
      if (diagramType == DiagramTypeEnum.externalCosts) {
        data.add(DiagramData(trips[i].mode, trips[i].costs.externalCosts.all));
      } else if (diagramType == DiagramTypeEnum.accidents) {
        data.add(
            DiagramData(trips[i].mode, trips[i].costs.externalCosts.accidents));
      } else if (diagramType == DiagramTypeEnum.air) {
        data.add(DiagramData(trips[i].mode, trips[i].costs.externalCosts.air));
      } else if (diagramType == DiagramTypeEnum.climate) {
        data.add(
            DiagramData(trips[i].mode, trips[i].costs.externalCosts.climate));
      } else if (diagramType == DiagramTypeEnum.noise) {
        data.add(
            DiagramData(trips[i].mode, trips[i].costs.externalCosts.noise));
      } else if (diagramType == DiagramTypeEnum.space) {
        data.add(
            DiagramData(trips[i].mode, trips[i].costs.externalCosts.space));
      } else if (diagramType == DiagramTypeEnum.barrier) {
        data.add(
            DiagramData(trips[i].mode, trips[i].costs.externalCosts.barrier));
      } else if (diagramType == DiagramTypeEnum.congestion) {
        data.add(DiagramData(
            trips[i].mode, trips[i].costs.externalCosts.congestion));
      } else if (diagramType == DiagramTypeEnum.internalCosts) {
        data.add(DiagramData(trips[i].mode, trips[i].costs.internalCosts.all));
      } else if (diagramType == DiagramTypeEnum.costs) {
        data.add(DiagramData(
            trips[i].mode,
            (trips[i].costs.internalCosts.all +
                trips[i].costs.externalCosts.all)));
      } else if (diagramType == DiagramTypeEnum.distance) {
        data.add(DiagramData(trips[i].mode, trips[i].distance));
      } else if (diagramType == DiagramTypeEnum.duration) {
        data.add(DiagramData(trips[i].mode, trips[i].duration));
      }
    }

    String unit = "";
    if (diagramType == DiagramTypeEnum.distance) {
      unit = 'km';
    } else if (diagramType == DiagramTypeEnum.duration) {
      unit = 'min';
    } else {
      unit = '€';
    }

    results.add(
      charts.Series<DiagramData, String>(
        id: 'data',
        colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
        domainFn: (DiagramData value, _) => value.dataName,
        measureFn: (DiagramData value, _) => value.value,
        data: data,
        labelAccessorFn: (DiagramData value, _) =>
            '${stringMappingHelper.mapModeStringToToolTip(value.dataName)}: ${value.value.toStringAsFixed(2)} $unit',
      ),
    );

    return results;
  }

  List<charts.Series<DiagramData, String>> createDiagramDataReversed(
      {required List<Trip> trips}) {
    List<charts.Series<DiagramData, String>> results = [];

    for (var i = 0; i < trips.length; i++) {
      final externalCostsData = [
        DiagramData('Luft', trips[i].costs.externalCosts.air),
        DiagramData('Lärm', trips[i].costs.externalCosts.noise),
        DiagramData('Klima', trips[i].costs.externalCosts.climate),
        DiagramData('Unfälle', trips[i].costs.externalCosts.accidents),
        DiagramData('Raum', trips[i].costs.externalCosts.space),
        DiagramData('Barriereeffekte', trips[i].costs.externalCosts.barrier),
        DiagramData('Stau', trips[i].costs.externalCosts.congestion),
      ];

      results.add(charts.Series<DiagramData, String>(
          id: trips[i].mode,
          domainFn: (DiagramData value, _) => value.dataName,
          measureFn: (DiagramData value, _) => value.value,
          data: externalCostsData));
    }
    return results;
  }
}

class DiagramData {
  final String dataName;
  final double value;

  DiagramData(this.dataName, this.value);
}
