import 'package:dartz/dartz.dart';
import 'package:multimodal_routeplanner/03_domain/entities/Trip.dart';
import 'package:multimodal_routeplanner/03_domain/repositories/route_repository.dart';

import '../../04_infrastructure/repositories/route_respoitory_impl.dart';
import '../entities/MobilityMode.dart';
import '../failure/failures.dart';

class RoutePlannerUsecases {
  final RouteRepository routeRepository = RouteRepositoryImpl();

  Future<Trip> getTrip(
      {required String startInput,
      required String endInput,
      required MobilityMode mode}) async {
    return routeRepository.getTripFromApi(
        startInput: startInput, endInput: endInput, mode: mode);
    // call function from repository

    // implement business logic

    // return Right(trip);
  }

  Map<String, Trip> getListAddedTrips(
      {required Map<String, Trip> trips, required Trip trip}) {
    Map<String, Trip> newTrips = trips;
    newTrips[trip.mode] = trip;

    List<Trip> sortedTrips = [];
    newTrips.values.toList().forEach((element) => sortedTrips.add(element));
    sortedTrips.sort(((a, b) =>
        a.costs.externalCosts.all.compareTo(b.costs.externalCosts.all)));

    Map<String, Trip> mapSortedTrips = {};
    for (var element in sortedTrips) {
      mapSortedTrips[element.mode] = element;
    }
    return mapSortedTrips;
  }

  Map<String, Trip> getListRemovedTrips(
      {required Map<String, Trip> trips, required String mode}) {

    trips.remove(mode);

    List<Trip> sortedTrips = [];
    trips.values.toList().forEach((element) => sortedTrips.add(element));
    sortedTrips.sort(((a, b) =>
        a.costs.externalCosts.all.compareTo(b.costs.externalCosts.all)));

    Map<String, Trip> mapSortedTrips = {};
    for (var element in sortedTrips) {
      mapSortedTrips[element.mode] = element;
    }
    return mapSortedTrips;
  }
}
