from dataclasses import dataclass

from ExternalCosts import ExternalCosts
from InternalCosts import InternalCosts


@dataclass
class Costs:
    internal_costs: InternalCosts
    external_costs: ExternalCosts
