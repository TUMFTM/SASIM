import 'package:multimodal_routeplanner/03_domain/entities/Costs/ExternalCosts.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Costs/InternalCosts.dart';

class Costs {
  final ExternalCosts externalCosts;
  final InternalCosts internalCosts;

  Costs({required this.externalCosts, required this.internalCosts});
}
