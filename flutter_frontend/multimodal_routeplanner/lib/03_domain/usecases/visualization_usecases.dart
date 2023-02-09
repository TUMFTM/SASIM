import '../entities/Trip.dart';

class VisualizationUsecases {
  Trip getFastestTrip({required List<Trip> trips}) {
    Trip fastestTrip = trips.reduce(
        (trip1, trip2) => trip1.duration < trip2.duration ? trip1 : trip2);

    return fastestTrip;
  }

  Trip getLowestExternalCostsTrip({required List<Trip> trips}) {
    Trip lowestExternalCostsTrip = trips.reduce((trip1, trip2) =>
        trip1.costs.externalCosts.all < trip2.costs.externalCosts.all
            ? trip1
            : trip2);

    return lowestExternalCostsTrip;
  }
}
