from dataclasses import dataclass

# external costs are costs, that are not directly paid for, but are beared by society.
# All vaules in this class are in €
@dataclass
class ExternalCosts:
    air: float
    noise: float
    accidents: float
    environment: float
    upstream: float