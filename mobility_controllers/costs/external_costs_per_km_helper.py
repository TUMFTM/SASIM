### external costs ### external costs ### external costs ### external costs

from classes.Enum.VehicleType import IndividualVehicleType, UrbanPublicVehicleType
from classes.Costs.ExternalCosts import ExternalCosts
from classes.Costs.InternalCosts import InternalCosts
from classes.Enum.PropulsionType import PropulsionType

import pandas as pd
import numpy as np
import os
from config.definitions import ROOT_DIR
import csv

# import external costs DB here from local csv file
from classes.Vehicle.Vehicle import Vehicle

internal_costs_path = os.path.join(ROOT_DIR, 'costs_db', 'db_internal_costs.csv')

external_costs_path = os.path.join(ROOT_DIR, 'costs_db', 'db_external_costs.csv')


df_db_external_costs = pd.read_csv(external_costs_path,
                                   delimiter=",", index_col=0)

df_db_internal_costs = pd.read_csv(internal_costs_path,
                                   delimiter=",", index_col=0)

df_db_external_costs = df_db_external_costs.astype(float) / 100
df_db_internal_costs = df_db_internal_costs.astype(float) / 100


def fetch_external_costs(distance: float, db_segment_type: str) -> ExternalCosts:
    costs_per_km = np.array(df_db_external_costs.loc[db_segment_type].tolist())
    costs = costs_per_km * distance

    external_costs = ExternalCosts(costs[0], costs[1], costs[2], costs[3], costs[4], costs[5], costs[6])

    return external_costs


def calculate_external_costs(distance: float, vehicle: Vehicle) -> ExternalCosts:
    vehicle_type = vehicle.get_vehicle_type()
    propulsion_type = vehicle.get_propulsion_type()
    is_sharing = vehicle.is_sharing()

    if (type(vehicle_type) == IndividualVehicleType):

        if (vehicle_type == IndividualVehicleType.BICYCLE):
            external_costs = calculate_external_costs_bicycle(distance=distance, propulsion_type=propulsion_type,
                                                              is_sharing=is_sharing)

        elif (vehicle_type == IndividualVehicleType.CAR):
            external_costs = calculate_external_costs_car(distance=distance, propulsion_type=propulsion_type,
                                                          is_sharing=is_sharing)

        elif (vehicle_type == IndividualVehicleType.MOPED):
            external_costs = calculate_external_costs_moped(distance=distance, propulsion_type=propulsion_type,
                                                            is_sharing=is_sharing)

        elif (vehicle_type == IndividualVehicleType.ESCOOTER):
            external_costs = calculate_external_costs_escooter(distance=distance, is_sharing=is_sharing)

        elif (vehicle_type == IndividualVehicleType.MOTORBIKE):
            external_costs = calculate_external_costs_motorbike(distance=distance)

        elif (vehicle_type == IndividualVehicleType.WALK):
            external_costs = calculate_external_costs_walk(distance=distance)
        else:
            print("VehicleType bei der Berechnung der externen Kosten nicht vorhanden")
            external_costs = None

    elif (type(vehicle_type) == UrbanPublicVehicleType):

        if (vehicle_type == UrbanPublicVehicleType.UBAHN):
            external_costs = calculate_external_costs_subway(distance)

        elif (vehicle_type == UrbanPublicVehicleType.SBAHN):
            external_costs = calculate_external_costs_regional_train(distance)

        elif (vehicle_type == UrbanPublicVehicleType.BUS):
            external_costs = calculate_external_costs_bus(distance)

        elif (vehicle_type == UrbanPublicVehicleType.TRAM):
            external_costs = calculate_external_costs_tram(distance)
        else:
            print("VehicleType bei der Berechnung der externen Kosten nicht vorhanden")
            external_costs = None

    else:
        print("Externe Kosten: keinen passenden VehicleType gefunden")
        external_costs = None

    return external_costs

def calculate_external_costs_car(distance: float, propulsion_type: PropulsionType,
                                 is_sharing: bool) -> ExternalCosts or None:
    if (is_sharing == True):
        return fetch_external_costs(distance, 'CAR_SHARING')

    else:
        if (propulsion_type == PropulsionType.ELECTRIC):
            return fetch_external_costs(distance, 'CAR_BEV')

        elif (propulsion_type == PropulsionType.PETROL):
            return fetch_external_costs(distance, 'CAR_GASOLINE')

        elif (propulsion_type == PropulsionType.DIESEL):
            return fetch_external_costs(distance, 'CAR_DIESEL')

        else:
            print("keine Kosten für angegebenen PKW Antrieb gefunden")
            return None


def calculate_external_costs_moped(distance: float, propulsion_type: PropulsionType,
                                   is_sharing: bool) -> ExternalCosts:
    if (is_sharing == True):

        return fetch_external_costs(distance, 'MOPED_SHARING')

    else:
        if (propulsion_type == PropulsionType.ELECTRIC):

            return fetch_external_costs(distance, 'EMOPED')

        elif (propulsion_type == PropulsionType.PETROL):

            return fetch_external_costs(distance, 'MOPED')


def calculate_external_costs_escooter(distance: float, is_sharing: bool) -> ExternalCosts:
    if (is_sharing == True):
        return fetch_external_costs(distance, 'ESCOOTER_SHARING')

    else:
        return fetch_external_costs(distance, 'ESCOOTER')


def calculate_external_costs_bicycle(distance: float, propulsion_type: PropulsionType,
                                     is_sharing: bool) -> ExternalCosts:
    if (is_sharing == True):

        if (propulsion_type == PropulsionType.ELECTRIC):
            return fetch_external_costs(distance, 'EBICYCLE_SHARING')

        elif (propulsion_type == PropulsionType.MUSCLE):
            return fetch_external_costs(distance, 'BICYCLE_SHARING')

    else:

        if (propulsion_type == PropulsionType.ELECTRIC):
            return fetch_external_costs(distance, 'EBICYCLE')

        elif (propulsion_type == PropulsionType.MUSCLE):
            return fetch_external_costs(distance, 'BICYCLE')


def calculate_external_costs_motorbike(distance: float, ) -> ExternalCosts:
    return fetch_external_costs(distance, 'MOTORCYCLE')


def calculate_external_costs_walk(distance: float, ) -> ExternalCosts:
    return fetch_external_costs(distance, 'WALKING')


def calculate_external_costs_subway(distance: float) -> ExternalCosts:
    return fetch_external_costs(distance, 'SUBWAY')


def calculate_external_costs_regional_train(distance: float) -> ExternalCosts:
    return fetch_external_costs(distance, 'REGIONAL_TRAIN')


def calculate_external_costs_tram(distance: float) -> ExternalCosts:
    return fetch_external_costs(distance, 'TRAM')


def calculate_external_costs_bus(distance: float) -> ExternalCosts:
    return fetch_external_costs(distance, 'BUS')


def calculate_external_costs_ebus(distance: float) -> ExternalCosts:
    return fetch_external_costs(distance, 'EBUS')
