class MvvController:

    def __init__(self, start_location: Location, end_location: Location):
        pass

    # TODO: add a time format to input variables

    # TODO: this needs to be a list of a list of waypoints
    def get_mvv_waypoints(self) -> List[List[Location]]:
        pass

    def get_mvv_modes(self)->  List[PublicTransportMode]:
        pass

    def get_from_tarif_zone(self)-> MvvTarifZone:
        pass

    def get_to_tarif_zone(self)-> MvvTarifZone:
        pass

    def get_durations(self)-> List[float]:
        pass

    def get_distances(self)-> List[float]:
        pass
