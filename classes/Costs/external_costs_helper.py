from classes.Costs.ExternalCosts import ExternalCosts


def add_external_costs(external_costs: ExternalCosts, i_external_costs: ExternalCosts):
    air_pollution = external_costs.air_pollution + i_external_costs.air_pollution
    noise_pollution = external_costs.noise_pollution + i_external_costs.noise_pollution
    climate = external_costs.climate + i_external_costs.climate
    accidents = external_costs.accidents + i_external_costs.accidents
    space = external_costs.space + i_external_costs.space
    barrier = external_costs.barrier + i_external_costs.barrier
    congestion = external_costs.congestion + i_external_costs.congestion

    sum_external_costs: ExternalCosts = ExternalCosts(
        air_pollution=air_pollution,
        noise_pollution=noise_pollution,
        climate=climate,
        accidents=accidents,
        space=space,
        barrier=barrier,
        congestion=congestion)

    return sum_external_costs
