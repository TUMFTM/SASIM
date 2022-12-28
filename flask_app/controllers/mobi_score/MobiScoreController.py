import os

import pandas as pd

from model.entities.costs.ExternalCosts import ExternalCosts
from model.enums.mobi_score.MobiScore import MobiScore
from config.definitions import ROOT_DIR


class MobiScoreController:
    def __init__(self):
        self._df_db_mobi_score = self._initialise_db()

    def get_mobi_score(self, external_costs: ExternalCosts, direct_distance: float) -> MobiScore:

        # unit is €-ct
        # /1000 km --> meters (direct distance)
        # /100 € --> €-ct (lower limit)
        b_lower_limit = self._df_db_mobi_score['LOWER_LIMIT']['B'] * direct_distance/1000/100
        c_lower_limit = self._df_db_mobi_score['LOWER_LIMIT']['C'] * direct_distance/1000/100
        d_lower_limit = self._df_db_mobi_score['LOWER_LIMIT']['D'] * direct_distance/1000/100
        e_lower_limit = self._df_db_mobi_score['LOWER_LIMIT']['E'] * direct_distance/1000/100

        if (external_costs.external_costs <= b_lower_limit):
            mobi_score = MobiScore.A

        elif(external_costs.external_costs > b_lower_limit and external_costs.external_costs <= c_lower_limit):
            mobi_score = MobiScore.B

        elif(external_costs.external_costs > c_lower_limit and external_costs.external_costs <= d_lower_limit):
            mobi_score = MobiScore.C

        elif(external_costs.external_costs > d_lower_limit and external_costs.external_costs <= e_lower_limit):
            mobi_score = MobiScore.D

        elif(external_costs.external_costs > e_lower_limit):
            mobi_score = MobiScore.E

        else:
            print("ERROR: external costs value not valid for mobi score calcuation")
            mobi_score = None

        return mobi_score

    def _initialise_db(self):
        # mobi_score_path = os.path.join(ROOT_DIR, 'multimodal-costbased-routeplanner', 'db', 'mobi_score', 'mobi_score.csv')

        # heroku deployment path
        mobi_score_path = os.path.join(ROOT_DIR, 'db', 'mobi_score', 'mobi_score.csv')

        df_db_mobi_score = pd.read_csv(mobi_score_path, delimiter=",", index_col=0)

        return df_db_mobi_score

