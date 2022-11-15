class CostsController:

    def __init__(self):
        pass

    def get_external_costs(self, distance: float, mode: ModeType) -> ExternalCosts:
        pass

    def get_internal_costs(self, distance: float, duration: float, mode: ModeType) -> InternalCosts:
        pass

    def get_internal_public_transport_costs(self, from_tarif_zone: TarifZone, to_tarif_zone: TarifZone) -> InternalCosts:
        pass


costs_controller = CostsController()