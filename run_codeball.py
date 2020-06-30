import json
import codeball.patterns as patt
import codeball.utils as utils
import codeball.models as models


# Define game files to process
xml_file = (
    r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/xml_file.xml"
)
txt_file = (
    r"c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/txt_file.txt"
)

game_dataset = utils.initialize_game_dataset(xml_file, txt_file)

# Initialize patterns that I want to process
pattern = models.Pattern("Team Stretched", "MET_001")
pattern.pattern_analysis = [
    patt.TeamStretched(game_dataset, pattern, team_code="home", threshold=40)
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
    json.dump(for_json_file, f, cls=utils.DataClassEncoder, indent=4)
