import shutil
from typing import Union
import uuid
import traceback

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

from scripts import api_to_csv
from utils.conversion_utils import createdir, get_generated_csv_filename
from utils.constants import DATA_DIRECTORY_NAME, CSV_OUTPUT_FILE_NAME



app = FastAPI()


@app.get("/")
def homepage():
    return {
        "message" : "Hi, welcome to the Data Downloader!"
    }


@app.post("/api_to_csv/")
def api_to_csv_converter(background_tasks: BackgroundTasks, api : str = Form(), username: Union[str,None] = Form(None), password: Union[str,None] = Form(None)):

    uid = str(uuid.uuid4())
    data_dir_name_with_uid = DATA_DIRECTORY_NAME + "-" + uid
    createdir(data_dir_name_with_uid)

    try:
        data = api_to_csv.get_data_from_api(api, username, password, data_dir_name_with_uid)

    except Exception as e:
        traceback.print_exc()
        background_tasks.add_task(shutil.rmtree, path = data_dir_name_with_uid)
        return {
            "error" : str(e)
        }

    csv_generated_filename = get_generated_csv_filename(data_dir_name_with_uid)
    headers = {'Content-Disposition': f'attachment; filename="{CSV_OUTPUT_FILE_NAME}"'}

    background_tasks.add_task(shutil.rmtree, path = data_dir_name_with_uid)
    return FileResponse(csv_generated_filename, headers=headers, media_type="text/csv")

