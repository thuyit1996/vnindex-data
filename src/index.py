# from requests
# from flask import request
import requests
from vnstock import *
from fastapi import FastAPI
from src.dtos.ISayHelloDto import ISayHelloDto

app = FastAPI()

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'X-Fiin-Key': 'KEY',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Fiin-User-ID': 'ID',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'X-Fiin-Seed': 'SEED',
    'sec-ch-ua-platform': 'Windows',
    'Origin': 'https://iboard.ssi.com.vn',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://iboard.ssi.com.vn/',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7'
}


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
