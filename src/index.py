# from requests
# from flask import request
import requests
from src.stock1 import *
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
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
    'x-refresh-token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjIzNzA5NSIsInV1aWQiOiI3YTM2YWZkZi1iNWZmLTQ3YTgtYWNlYy1hZjlmNzVlM2I0ODMiLCJjaGFubmVsIjoid2ViIiwiaWF0IjoxNjg1ODU4NDY4LCJleHAiOjE2ODU4ODcyNjh9.zHTccOa1Pak18QBQywITF7guoE-hd_HVDMJY287l388",
    "x-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjIzNzA5NSIsInV1aWQiOiIwNDBkNmE5Yy03Mjc3LTQwN2EtOTkyOC1kZmIzYzM2MzA2NjYiLCJjaGFubmVsIjoid2ViIiwiaWF0IjoxNjg1ODU4NDY4LCJleHAiOjE2ODU4ODcyNjh9.Wx3sRVqAs_3fjFLJ6KqOuBAz2zrUmRXMS5aZT5sgzME"
}


@app.get("/get-vnindex")
async def root():
    # url = "https://fiin-market.ssi.com.vn/MarketInDepth/GetIndexSeries?language=vi&ComGroupCode=VNINDEX&TimeRange=OneYear&id=1"
    # response = requests.get(url, headers=headers)
    # print(response.status_code)
    print(get_index_series())
    return 1


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}
