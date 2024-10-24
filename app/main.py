from typing import Union
from fastapi import FastAPI
from Mangum import mangum

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Welcome to AT"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

handler = Mangum(app)

