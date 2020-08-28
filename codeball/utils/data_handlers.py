"""
    Auxiliar methods to work with the data.

"""
from typing import List
import pandas as pd


def find_intervals(
    boolean_series: pd.DataFrame, minimum_interval: float = 5
) -> List:
    intervals = []
    interval_open = False
    for i, f in enumerate(boolean_series):
        if f is True and interval_open is False:
            interval_open = True
            start_interval = i
        elif f is False and interval_open is True:
            interval_open = False
            end_interval = i - 1
            # TODO change to be dependen on frame rate
            if (end_interval - start_interval) > 25 * minimum_interval:
                intervals.append([start_interval, end_interval])

    return intervals


def frame_to_milisecond(frame: int, frame_rate: float) -> float:
    return frame * 1000 / frame_rate
