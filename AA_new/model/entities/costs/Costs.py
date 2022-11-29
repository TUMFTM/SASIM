from dataclasses import dataclass

from AA_new.model.entities.costs.ExternalCosts import ExternalCosts
from AA_new.model.entities.costs.InternalCosts import InternalCosts


@dataclass
class Costs:
    internal_costs: InternalCosts = InternalCosts(internal_costs=0)
    external_costs: ExternalCosts = ExternalCosts(
            external_costs=0,
            air=0,
            noise=0,
            climate=0,
            accidents=0,
            space=0,
            barrier=0,
            congestion=0
        )



    def __add__(self, other):
        return Costs(
            internal_costs= self.internal_costs + other.internal_costs,
            external_costs=self.external_costs + other.external_costs
        )


