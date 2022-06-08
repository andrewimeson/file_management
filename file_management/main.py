from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ManageFile(BaseModel):
    action: str


@app.get("/")
async def index():
    """Basic hellow world index"""
    return {"Hello": "World"}


@app.post("/manage_file")
async def read_action(action: ManageFile):
    """
    Returns an example text file, or updates the version that the server has
    """
    if action.action == "read":
        return {"i_should": "Read"}
    elif action.action == "download":
        return {"i_should": "Download"}
    return {"success": True}
