from dataclasses import dataclass

@dataclass
class ExternalCosts:
    air_pollution: float = 0
    noise_pollution: float = 0
    climate: float = 0
    accidents: float = 0
    space: float = 0
    barrier: float = 0
    congestion: float = 0

    # all costs are all above except health costs
    @property
    def all(self):
        all: float = self.air_pollution + self.noise_pollution + self.climate \
                     + self.congestion + self.accidents + self.space + self.barrier
        return all
