import json
import requests

from utils.conversion_utils import convert_json_to_csv, createdir

from utils.constants import INPUT_FILE_NAME, JSON_DATA_FOLDER, CSV_DATA_FOLDER


def get_data_from_api(api:str, username:str, password:str, data_dir_name_with_uid:str) -> dict:

    if username and password: 
        response = requests.get(api, auth=(username, password))

    else:
        response = requests.get(api)
    
    
    try:    
        data = response.json()

    except Exception as e:
        print(f"Error occured in {api} api - {e}")
        return 


    # store the data in json and convert it into csv 
    file_json = f"{data_dir_name_with_uid}/{JSON_DATA_FOLDER}/{INPUT_FILE_NAME}.json"
    file_csv = f"{data_dir_name_with_uid}/{CSV_DATA_FOLDER}/{INPUT_FILE_NAME}.csv"

    with open(file_json, 'w') as file:
        json.dump(data, file)
    convert_json_to_csv(file_json, output_file=file_csv)
    

    return data




if __name__ == "__main__":
    pass
    



