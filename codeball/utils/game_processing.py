import json
from kloppy import load_epts_tracking_data, to_pandas
import codeball.models as models
import codeball.utils as utils


def initialize_game_dataset(
    tracking_meta_data_file: str, tracking_data_file: str
) -> models.GameDataset:

    tracking_data_package = _initialize_data_package(
        data_type=models.DataType.TRACKING,
        data_file=tracking_data_file,
        meta_data_file=tracking_meta_data_file,
    )

    return models.GameDataset(tracking_data=tracking_data_package)


def _initialize_data_package(
    data_type: models.DataType, data_file: str, meta_data_file: str
) -> models.DataPackage:

    data_package = models.DataPackage(
        data_type=data_type,
        data_file=data_file,
        meta_data_file=meta_data_file,
    )

    data_package.load_dataset()

    data_package.build_dataframe()

    return data_package


def save_patterns_for_play(game_dataset: models.GameDataset, file_path: str):
    events_for_json = _get_event_for_json(game_dataset)
    patterns_config = _get_patterns_config(game_dataset)

    json_file_data = {
        "events": events_for_json,
        "insert": {"patterns": patterns_config},
    }

    with open(file_path, "w") as f:
        json.dump(json_file_data, f, cls=utils.DataClassEncoder, indent=4)


def _get_event_for_json(game_dataset: models.GameDataset):
    events_for_json = []
    for pattern in game_dataset.patterns:
        events_for_json = events_for_json + pattern.events

    return events_for_json


def _get_patterns_config(game_dataset: models.GameDataset):
    patterns_config = []
    for pattern in game_dataset.patterns_config:
        pattern_config = {"name": pattern["name"], "code": pattern["code"]}
        patterns_config.append(pattern_config)

    return patterns_config
