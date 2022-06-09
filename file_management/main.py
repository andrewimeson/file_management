import os
from enum import Enum

import requests
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

description = """
Manages a lorem ipsum file for your reading

## About

See [the GitHub repo](https://github.com/andrewimeson/file_management) for more
information.
"""

app = FastAPI(
    title="File Management API",
    description=description,
    contact={"name": "Andrew Imeson", "url": "https://andrewimeson.com/"},
)


class FileAction(str, Enum):
    download = "download"
    read = "read"


class ManageFile(BaseModel):
    action: FileAction

    class Config:
        use_enum_values = True


# This is not the best place to store this...
file_name = "sample-text-file.txt"
file_path = "data/" + file_name


def get_sample_file():
    """
    Downloads sample text file and stores on the local filesystem
    """
    url_prefix = "https://www.learningcontainer.com/wp-content/uploads/2020/04/"
    url = url_prefix + file_name
    r = requests.get(url)
    if r.status_code == 200:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            file.write(r.content)


@app.get("/")
async def index():
    """Index page redirect to docs"""
    return RedirectResponse("/docs/")


@app.post("/manage_file")
async def manage_file(action: ManageFile):
    """
    Returns an example text file, or updates the version that the server has
    """
    if action.action == FileAction.read:
        with open(file_path) as file:
            data = {"content": file.read()}
            return data
    elif action.action == FileAction.download:
        get_sample_file()
        return {"i_should": "Download"}
