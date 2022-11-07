from classes.Enum.SharingCompany import SharingCompany
from classes.Enum.TarifZoneMVV import TarifZoneMVV
from classes.Enum.VehicleType import IndividualVehicleType
from classes.Enum.PropulsionType import PropulsionType

import pandas as pd
import math
import os

from classes.Vehicle.IndividualVehicle import IndividualVehicle
from classes.Vehicle.SharingVehicle import SharingVehicle
from classes.Vehicle.UrbanPublicVehicle import UrbanPublicVehicle
from config.definitions import ROOT_DIR

# import external costs DB here from local csv file

internal_costs_path = os.path.join(ROOT_DIR, 'costs_db', 'db_internal_costs.csv')
internal_costs_mvv_path = os.path.join(ROOT_DIR, 'costs_db', 'db_internal_costs_mvv.csv')

df_db_internal_costs = pd.read_csv(internal_costs_path,
                                   delimiter=",", index_col=0)

df_db_internal_costs_mvv = pd.read_csv(internal_costs_mvv_path,
                                   delimiter=",", index_col=0)


def fetch_internal_costs(mode: str, internal_cost_type: str) -> float:
    costs_per_x = df_db_internal_costs.loc[mode][internal_cost_type]
    return costs_per_x

def fetch_internal_costs_mvv(tarif_zone: str) -> float:
    costs_per_trip = df_db_internal_costs_mvv.loc[tarif_zone]['TICKET']
    return costs_per_trip

def calculate_internal_costs(vehicle: IndividualVehicle or SharingVehicle or UrbanPublicVehicle,
                             tarif_zone: str = None, distance: float = None,
                             duration: float = None):
    vehicle_type = vehicle.get_vehicle_type()
    propulsion_type = vehicle.get_propulsion_type()

    if (type(vehicle) == IndividualVehicle):

        if (vehicle_type == IndividualVehicleType.BICYCLE):
            return calculate_internal_costs_bicycle(distance, propulsion_type)

        elif (vehicle_type == IndividualVehicleType.CAR):
            return calculate_internal_costs_car(distance, propulsion_type)

        elif (vehicle_type == IndividualVehicleType.MOPED):
            return calculate_internal_costs_moped(distance, propulsion_type)


        elif (vehicle_type == IndividualVehicleType.WALK):
            internal_costs: float = 0.0
            return internal_costs

        else:
            print("Externe Kosten: keinen passenden VehicleType gefunden")

    elif (type(vehicle) == UrbanPublicVehicle):

        return calculate_internal_costs_public_transport(tarif_zone=tarif_zone)

    elif (type(vehicle) == SharingVehicle):
        if (vehicle.get_company_name() == SharingCompany.CAB):
            return calculate_internal_costs_sharing(distance=distance, duration=duration, company="CAB")

        elif (vehicle.get_company_name() == SharingCompany.EMMY):

            return calculate_internal_costs_sharing(distance=distance, duration=duration, company="EMMY")

        elif (vehicle.get_company_name() == SharingCompany.FLINKSTER):
            return calculate_internal_costs_sharing(distance=distance, duration=duration, company="FLINKSTER")

        elif (vehicle.get_company_name() == SharingCompany.SHARENOW):
            return calculate_internal_costs_sharing(distance=distance, duration=duration, company="SHARENOW")

        elif (vehicle.get_company_name() == SharingCompany.TIER):
            return calculate_internal_costs_sharing(distance=distance, duration=duration, company="TIER")

        else:
            print("Externe Kosten: keinen passenden VehicleType gefunden")


    else:
        print("Externe Kosten: keinen passenden VehicleType gefunden")

# general formula for sharing trips, that can contain time- and distance-dependent costs,
# and also include a fee per ride and a maximum price

def calculate_internal_costs_sharing(distance: float, duration: float, company: str) -> float:
    internal_costs_per_km = fetch_internal_costs(company, 'PER_KM')
    internal_costs_per_ride = fetch_internal_costs(company, 'PER_RIDE')
    internal_costs_per_minute = fetch_internal_costs(company, 'PER_MINUTE')
    internal_costs_per_quarter_hour = fetch_internal_costs(company, 'PER_QUARTER_HOUR')
    internal_costs_per_hour = fetch_internal_costs(company, 'PER_HOUR')
    internal_costs_max = fetch_internal_costs(company, 'MAX_COSTS')

    internal_costs = internal_costs_per_ride + internal_costs_per_minute * math.ceil(duration) + \
                     internal_costs_per_quarter_hour * math.ceil(duration/15) + \
                     internal_costs_per_hour * math.ceil(duration/60) + internal_costs_per_km * distance



    if (internal_costs_max != 0 and internal_costs > internal_costs_max):
        internal_costs = internal_costs_max

    return internal_costs

# internal costs for privately owned vehicles
def calculate_internal_costs_car(distance: float, propulsionType: PropulsionType) -> float:
    if (propulsionType == PropulsionType.ELECTRIC):
        return fetch_internal_costs('ECAR', 'PER_KM') * distance
    else:
        return fetch_internal_costs('CAR', 'PER_KM') * distance


def calculate_internal_costs_moped(distance: float, propulsionType: PropulsionType) -> float:
    if (propulsionType == PropulsionType.ELECTRIC):
        return fetch_internal_costs('EMOPED', 'PER_KM') * distance
    else:
        return fetch_internal_costs('MOPED', 'PER_KM') * distance


def calculate_internal_costs_bicycle(distance: float, propulsionType: PropulsionType) -> float:
    if (propulsionType == PropulsionType.ELECTRIC):
        return fetch_internal_costs('EBICYCLE', 'PER_KM') * distance
    else:
        return fetch_internal_costs('BICYCLE', 'PER_KM') * distance


# internal costs for public transport
def calculate_internal_costs_public_transport(tarif_zone: str) -> float:
    return fetch_internal_costs_mvv(tarif_zone=tarif_zone)
