from fastapi import FastAPI
from api.sel import sel
from api.angola import angola

app = FastAPI()


@app.get("/")
def read_root():
    return {"Ada": "TECMRDM"}


@app.get("/sel")
def read_sel():
    return {"title": sel()}


@app.get("/angola")
def read_angola():
    return {"title": angola()}
