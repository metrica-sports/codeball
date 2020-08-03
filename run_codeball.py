import pickle
import codeball.models as models
import codeball.patterns as patt
import codeball.utils as utils


initiaize_dataset = False
if initiaize_dataset:
    # Define game files to process
    metadata_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/metadata.xml"
    )
    tracking_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/tracking.txt"
    )
    events_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/events.json"
    )

    game_dataset = models.initialize_game_dataset(
        metadata_file=metadata_file,
        tracking_data_file=tracking_file,
        events_data_file=events_file,
    )

    with open(r"./codeball/tests/files/game_dataset.obj", "wb") as f:
        pickle.dump(game_dataset, f)

else:

    with open(r"./codeball/tests/files/game_dataset.obj", "rb") as f:
        game_dataset = pickle.load(f)

game_dataset.initialize_patterns()

game_dataset.run_patterns()

game_dataset.save_patterns_for_play("development_data.json")
