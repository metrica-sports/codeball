import pickle
from codeball.models import GameDataset, PatternsSet

initiaize_dataset = True
if initiaize_dataset:
    # Elite sample game
    metadata_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/metadata.xml"
    )
    tracking_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/tracking.txt"
    )
    events_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/events.json"
    )

    game_dataset = GameDataset(
        tracking_metadata_file=metadata_file,
        tracking_data_file=tracking_file,
        events_metadata_file=metadata_file,
        events_data_file=events_file,
    )

    with open(r"./codeball/tests/files/game_dataset.obj", "wb") as f:
        pickle.dump(game_dataset, f)


else:

    with open(r"./codeball/tests/files/game_dataset.obj", "rb") as f:
        game_dataset = pickle.load(f)

patterns_set = PatternsSet(game_dataset=game_dataset)

patterns_set.initialize_patterns()

patterns_set.run_patterns()

patterns_set.save_patterns_for_play("development_data.json")
