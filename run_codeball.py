import json
from kloppy import load_epts_tracking_data, to_pandas
from codeball.models.common import Pattern, GameDataset
from codeball.patterns.team_stretched import TeamStretched
from codeball.utils.json_encoders import DataClassEncoder


# Define game files to process
xml_file = r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/xml_file.xml"
txt_file = r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/txt_file.txt"

# Load data and transform it to a pandas dataframe
dataset = load_epts_tracking_data(xml_file, txt_file)
dataframe = to_pandas(dataset)

# Initialize game dataset and add patterns
game_dataset = GameDataset(dataframe)

# Initialize patterns that I want to process
pattern = Pattern("Team Stretched", "MET_001")
pattern.pattern_analysis = [
    TeamStretched(game_dataset, pattern, options={"team": "home", "threshold": 0.4})
]

game_dataset.patterns = [pattern]

# Run patterns for the game dataset
for p in game_dataset.patterns:
    for a in p.pattern_analysis:
        pattern_events = a.run()
        p.events = p.events + pattern_events

# Save events to json file for metrica play
events_for_json = []
for p in game_dataset.patterns:
    events_for_json = events_for_json + p.events

for_json_file = {
    "events": events_for_json,
    "insert": {"patterns": [{"name": "Team stretched", "code": "MET_001"}]},
}

with open("data.json", "w") as f:
    json.dump(for_json_file, f, cls=DataClassEncoder, indent=4)
