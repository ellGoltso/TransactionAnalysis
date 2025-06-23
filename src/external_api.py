import os

import requests
from dotenv import load_dotenv
import json


def get_share_price() -> list[dict]:
    """ Возвращает список словарей с названиями акций и ценами на них """

    with open("user_settings.json") as f:
        settings = json.load(f)
    symbols = settings["user_stocks"]

    load_dotenv()
    api_key = os.getenv("API_KEY_STOCKS")

    stock_prices = []
    for stock_symbol in symbols:
        url = f"https://financialmodelingprep.com/stable/profile?symbol={stock_symbol}&apikey={api_key}"
        response = (requests.request("GET", url)).json()
        price_dict = {"stock": stock_symbol, "price": round(float(response[0]["price"]), 2)}
        stock_prices.append(price_dict)

    return stock_prices


def get_exchange_rate() -> list[dict]:
    """ Возвращает список словарей с названием валюты и курсом относительно рубля """

    with open("user_settings.json") as f:
        settings = json.load(f)
    currency = settings["user_currencies"]

    load_dotenv()
    api_key = os.getenv("APIKEY_EXCHANGE")
    headers = {
        "apikey": api_key
    }

    currency_rates = []
    for i in currency:
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={i}"
        response = (requests.request("GET", url, headers=headers)).json()
        rate = response["rates"]
        dict_rate = {"currency": i, "rate": rate["RUB"]}
        currency_rates.append(dict_rate)

    return currency_rates

