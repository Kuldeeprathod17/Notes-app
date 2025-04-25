from typing import Union

from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse

from pymongo import MongoClient


app = FastAPI()


conn=MongoClient("mongodb+srv://kuldeep:kuldeep_1710@cluster0.x5quxjp.mongodb.net/Notes")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}




# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}