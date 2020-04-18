import xml.etree.ElementTree as et
import numpy as np 
import pandas as pd 

def read_fifa_format(xml_file, txt_file):
    
    metadata_dict   = get_dict_from_xml(xml_file)
    data_frame      = get_data_frames_from_txt(txt_file)

    return metadata_dict, data_frame


def get_dict_from_xml(xml_file):
    
    metadata_dic = dict()

    fifa_feed = et.ElementTree(file=xml_file).getroot()

    for child in fifa_feed:

        print(child)
        for grchild in child:
            print(grchild.tag)

    return metadata_dic


def get_data_frames_from_txt(text_file):
    
    data_frame = pd.DataFrame()

    return data_frame