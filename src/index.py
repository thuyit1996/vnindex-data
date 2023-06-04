# from requests
# from flask import request
from pandas import *
from json import *
from vnstock import *
from fastapi import FastAPI
from src.dtos.ISayHelloDto import ISayHelloDto

app = FastAPI()

@app.get("/get-vnindex")
async def root():
    # url = "https://fiin-market.ssi.com.vn/MarketInDepth/GetIndexSeries?language=vi&ComGroupCode=VNINDEX&TimeRange=OneYear&id=1"
    # response = requests.get(url, headers=headers)
    # print(response)
    # return response
    df = get_index_series(index_code='VNINDEX', time_range='OneYear')
    return df



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
