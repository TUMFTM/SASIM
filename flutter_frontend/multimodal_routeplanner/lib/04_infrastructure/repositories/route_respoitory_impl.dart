import 'package:multimodal_routeplanner/03_domain/failure/failures.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';
import 'package:dartz/dartz.dart';
import 'package:multimodal_routeplanner/03_domain/repositories/route_repository.dart';
import 'package:multimodal_routeplanner/04_infrastructure/datasources/route_remote_datasource.dart';

import '../../03_domain/entities/MobilityMode.dart';

class RouteRepositoryImpl implements RouteRepository {
  final RouteRemoteDatasource routeRemoteDatasource =
      RouteRemoteDatasourceImpl();

  @override
  Future<Trip> getTripFromApi(
      {required String startInput,
      required String endInput,
      required MobilityMode mode}) async {
    final remoteTrip = await routeRemoteDatasource.getSingleRouteFromApi(
        startInput: startInput, endInput: endInput, mode: mode);

    return remoteTrip;
  }
}
