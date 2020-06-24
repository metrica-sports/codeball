"""
    Methods to handle data. Actions like:
        - Filter per team
        - Find intervals
        - Etc
"""
from typing import List
import pandas as pd
from codeball.models import GameDataset


def get_team_dataframe(
    dataframe: pd.DataFrame, team_code: str
) -> pd.DataFrame:
    match_string = team_code + "_[0-9]+_x"
    # TODO Also filter goalkeeper so only field players left
    team_dataframe = dataframe.filter(regex=match_string)
    return team_dataframe


def find_intervals(boolean_series: pd.DataFrame) -> List:
    intervals = []
    interval_open = False
    for i, f in enumerate(boolean_series):
        if f is True and interval_open is False:
            interval_open = True
            start_interval = i
        elif f is False and interval_open is True:
            interval_open = False
            intervals.append([start_interval, i - 1])

    return intervals
