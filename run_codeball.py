from kloppy import load_epts_tracking_data, to_pandas
from codeball.models.common import Pattern, GameDataset
from codeball.patterns.team_stretched import TeamStretched

xml_file =r'c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/xml_file.xml'
txt_file =r'c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/txt_file.txt'

dataset = load_epts_tracking_data(xml_file, txt_file)
dataframe = to_pandas(dataset)

game_dataset = GameDataset(dataframe)

pattern = Pattern("Team Stretched","MET_001")

pattern.pattern_analysis =[TeamStretched(
    game_dataset,
    pattern,
    options={"team": "home", "threshold": 0.4}
)]

game_dataset.patterns =[pattern]

for p in game_dataset.patterns:
    for a in p.pattern_analysis:
        a.run()