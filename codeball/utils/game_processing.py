from kloppy import load_epts_tracking_data, to_pandas
import codeball.models as models


def initialize_game_dataset(xml_file, txt_file) -> models.GameDataset:

    # Load data and transform it to a pandas dataframe
    dataset = load_epts_tracking_data(xml_file, txt_file)
    dataframe = to_pandas(dataset)

    # Initialize game dataset and add patterns
    return models.GameDataset(dataframe)
