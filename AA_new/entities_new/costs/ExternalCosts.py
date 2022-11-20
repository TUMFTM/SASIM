from dataclasses import dataclass

# external costs are costs, that are not directly paid for, but are beared by society.
# All vaules in this class are in €
@dataclass
class ExternalCosts:
    external_costs: float = 0
    air: float = 0
    noise: float = 0
    climate: float = 0
    accidents: float = 0
    space: float = 0
    barrier: float = 0
    congestion: float = 0

    def __add__(self, other):
        return ExternalCosts(
            self.external_costs + other.external_costs,
            self.air + other.air,
            self.noise + other.noise,
            self.climate + other.climate,
            self.accidents + other.accidents,
            self.space + other.space,
            self.barrier + other.barrier,
            self.congestion + other.congestion
        )
