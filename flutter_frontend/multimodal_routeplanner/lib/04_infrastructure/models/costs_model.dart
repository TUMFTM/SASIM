import 'package:multimodal_routeplanner/03_domain/entities/Costs/Costs.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Costs/ExternalCosts.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Costs/InternalCosts.dart';
import 'package:multimodal_routeplanner/04_infrastructure/models/external_costs_model.dart';
import 'package:multimodal_routeplanner/04_infrastructure/models/internal_costs_model.dart';

class CostsModel extends Costs {
  CostsModel(
      {required ExternalCosts externalCosts,
      required InternalCosts internalCosts})
      : super(externalCosts: externalCosts, internalCosts: internalCosts);

  factory CostsModel.fromJson(Map<String, dynamic> json) {
    return CostsModel(
      externalCosts: ExternalCostsModel.fromJson(json['externalCosts']),
      internalCosts: InternalCostsModel.fromJson(json['internalCosts']),
    );
  }
}
