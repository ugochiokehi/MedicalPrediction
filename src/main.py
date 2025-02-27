# from typing import Union
from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)
import  debugpy
debugpy.listen("0.0.00", 5678)
@app.get("/")
def read_root():
    return {"Hello": "World1234diwn"}

@app.get("/hits")
def read_hits():
    r.incr("hits")
    return {"number of hits": r.get("hits")}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
