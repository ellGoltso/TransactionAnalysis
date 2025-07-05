import datetime
import json

from src.external_api import get_exchange_rate, get_share_price
from src.utils import get_data_from_excel_file, get_general_information, get_greetings, get_top_five_transactions


def get_json_data(date: datetime.datetime):
    """Принимает дату и время возвращает json ответ с:
    приветствием
    информацией о картах с начала месяца
    топ 5 транзакций с начала месяца
    курсом валюты
    стоимостью акций"""

    greeting = {"greeting": get_greetings(date)}
    df_data = get_data_from_excel_file(date)
    cards = {"cards": get_general_information(df_data)}
    top_transactions = {"top_transactions": get_top_five_transactions(df_data)}

    currency_rates = {"currency_rates": get_exchange_rate()}
    stock_prices = {"stock_prices": get_share_price()}
    data = {**greeting, **cards, **top_transactions, **currency_rates, **stock_prices}

    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    return json_data


# date_t = datetime.datetime(2021, 12, 16, 16, 27, 0)
# print(get_json_data(date_t))
