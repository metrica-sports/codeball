import pickle
import codeball.models as models
import codeball.patterns as patt
import codeball.utils as utils


initiaize_dataset = True
if initiaize_dataset:
    # Define game files to process
    xml_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/xml_file.xml"
    )
    txt_file = (
        r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/txt_file.txt"
    )

    game_dataset = models.initialize_game_dataset(
        tracking_metadata_file=xml_file, tracking_data_file=txt_file
    )

    with open(r"./codeball/tests/files/game_dataset.obj", "wb") as f:
        pickle.dump(game_dataset, f)

else:

    with open(r"./codeball/tests/files/game_dataset.obj", "rb") as f:
        game_dataset = pickle.load(f)

game_dataset.initialize_patterns()

game_dataset.run_patterns()

game_dataset.save_patterns_for_play("development_data.json")
