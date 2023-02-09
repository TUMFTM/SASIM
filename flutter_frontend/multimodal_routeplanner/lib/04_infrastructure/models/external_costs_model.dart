import 'package:multimodal_routeplanner/03_domain/entities/Costs/ExternalCosts.dart';

class ExternalCostsModel extends ExternalCosts {
  ExternalCostsModel(
      {required double air,
      required double noise,
      required double climate,
      required double accidents,
      required double space,
      required double barrier,
      required double congestion,
      required double all})
      : super(
            air: air,
            noise: noise,
            climate: climate,
            accidents: accidents,
            space: space,
            barrier: barrier,
            congestion: congestion,
            all: all);

  factory ExternalCostsModel.fromJson(Map<String, dynamic> json) {
    return ExternalCostsModel(
        air: json['air'],
        noise: json['noise'],
        climate: json['climate'],
        accidents: json['accidents'],
        space: json['space'],
        barrier: json['barrier'],
        congestion: json['congestion'],
        all: json['all']);
  }
}
