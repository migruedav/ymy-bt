from fastapi import FastAPI
from api.sel import sel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Ada": "TECMRDM"}


@app.get("/sel")
def read_sel():
    return {"title": sel()}
