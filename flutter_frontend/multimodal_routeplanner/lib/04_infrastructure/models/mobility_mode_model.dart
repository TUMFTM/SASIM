import '../../03_domain/entities/MobilityMode.dart';
import '../../03_domain/enums/MobilityModeEnum.dart';

class MobilityModeModel extends MobilityMode {
  MobilityModeModel({required MobilityModeEnum mode}) : super(mode: mode);

  factory MobilityModeModel.fromJson(Map<String, dynamic> json) {
    return MobilityModeModel(mode: json['mode']);
  }
}
