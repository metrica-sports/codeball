import codeball.commons.io as io
from kloppy import (
    load_metrica_tracking_data, 
    load_tracab_tracking_data,
    load_epts_tracking_data, 
    load_statsbomb_event_data,
    to_pandas, 
    transform
)

# from kloppy import epts_load_meta_data, epts_read_raw_data

#  Sample game 3
xml_file ='c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/xml_file.xml'
txt_file ='c:/1_METRICA/1_ANALYSIS/sample-data/data/Sample_Game_3/txt_file.txt'

# # Kloppy
# xml_file = 'C:/1_METRICA/1_ANALYSIS/kloppy/examples/epts/epts_meta.xml'
# txt_file = 'C:/1_METRICA/1_ANALYSIS/kloppy/examples/epts/epts_raw.txt' 

# data = io.get_dict_from_xml(xml_file)`
dataset = load_epts_tracking_data(xml_file, txt_file)

print(dataset)
# # step 1: load metadata
# with open(xml_file, "rb") as meta_fp:
#     meta_data = epts_load_meta_data(meta_fp)

#  # step 5: put the records in a pandas dataframe
# with open(txt_file, "rb") as raw_fp:
#     # we are only interested in the data from the 'heartbeat' sensor
#     records = epts_read_raw_data(raw_fp, meta_data, sensor_ids=["position"])
#     data_frame = DataFrame.from_records(records)
    
# # Pfieh.. data. That's better :-)
#     print(data_frame.head())