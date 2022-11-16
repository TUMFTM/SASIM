from dataclasses import dataclass
# internal costs are costs, that are directly paid for.
# All vaules in this class are in €
@dataclass
class InternalCosts:
    internal_costs: float = 0

    def __add__(self, other):
        return InternalCosts(
            internal_costs=self.internal_costs + other.internal_costs
        )