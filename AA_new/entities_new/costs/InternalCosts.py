from dataclasses import dataclass
# internal costs are costs, that are directly paid for.
# All vaules in this class are in €
@dataclass
class InternalCosts:
    internal_costs: float