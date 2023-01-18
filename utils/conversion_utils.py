from typing import Union
import pandas as pd
import os

import json

from utils.constants import JSON_DATA_FOLDER, CSV_DATA_FOLDER, INPUT_FILE_NAME


def convert_json_to_csv(json_input_file: str, output_file:str) -> None:

    with open(json_input_file, 'r') as file:
        data = json.load(file)
    if isinstance(data, dict):
        data = pd.DataFrame.from_dict(data, orient='index')
    elif isinstance(data, list):
        data = pd.DataFrame.from_records(data)
    data.to_csv(output_file)

def createdir(data_dir_name_with_uid:str) -> None:
    os.makedirs(f"{data_dir_name_with_uid}", exist_ok=True)
    os.makedirs(f"{data_dir_name_with_uid}/{JSON_DATA_FOLDER}")
    os.makedirs(f"{data_dir_name_with_uid}/{CSV_DATA_FOLDER}")


def get_generated_csv_filename(data_directory_name:str):
    return f"{data_directory_name}/{CSV_DATA_FOLDER}/{INPUT_FILE_NAME}.csv"



