from kloppy import load_epts_tracking_data, to_pandas
import codeball.models as models


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
