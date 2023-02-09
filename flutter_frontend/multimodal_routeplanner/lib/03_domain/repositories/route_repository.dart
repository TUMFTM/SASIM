import '../entities/MobilityMode.dart';
import '../entities/Trip.dart';

abstract class RouteRepository {
  Future<Trip> getTripFromApi(
      {required String startInput,
      required String endInput,
      required MobilityMode mode});
}
