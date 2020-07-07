import json
import codeball.models as models
import codeball.patterns as patt
import codeball.utils as utils


# Define game files to process
xml_file = (
    r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/xml_file.xml"
)
txt_file = (
    r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/txt_file.txt"
)

game_dataset = utils.initialize_game_dataset(
    tracking_meta_data_file=xml_file, tracking_data_file=txt_file
)

game_dataset.initialize_patterns()

game_dataset.run_patterns()

# Save events to json file for metrica play
events_for_json = []
for p in game_dataset.patterns:
    events_for_json = events_for_json + p.events

# for_json_file = {
#     "events": events_for_json,
#     "insert": {"patterns": [{"name": "Team stretched", "code": "MET_001"}]},
# }

# with open("data.json", "w") as f:
#     json.dump(for_json_file, f, cls=utils.DataClassEncoder, indent=4)
