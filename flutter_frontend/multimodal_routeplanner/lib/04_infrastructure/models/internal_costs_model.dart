import '../../03_domain/entities/Costs/InternalCosts.dart';

class InternalCostsModel extends InternalCosts {
  InternalCostsModel({required double internalCosts})
      : super(all: internalCosts);

  factory InternalCostsModel.fromJson(Map<String, dynamic> json) {
    return InternalCostsModel(internalCosts: json['all']);
  }
}
