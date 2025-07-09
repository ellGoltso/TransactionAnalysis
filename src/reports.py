import datetime
import json
import logging
from typing import Optional

import pandas as pd

from src.decorators import write_to_file

reports_logger = logging.getLogger("reports")
file_handler = logging.FileHandler("logs/reports.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
reports_logger.addHandler(file_handler)
reports_logger.setLevel(logging.DEBUG)


@write_to_file()
def spending_by_category(transactions: pd.DataFrame, category: str = None, date: Optional[str] = None) -> pd.DataFrame:
    """Функция принимает на вход:
        датафрейм с транзакциями,
        опционально название категории(если не передана берется по умолчанию из json файла user_settings.json по ключу: user_category),
        опциональную дату.
    Если дата не передана, то берется текущая дата.
    Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)"""

    if category is None:
        with open("user_settings.json", "r", encoding="utf-8") as f:
            settings = json.load(f)
        category = settings["user_category"]

    if date is None:
        date_obj = datetime.date.today()
    else:
        date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
    date_obj = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, hour=23, minute=59, second=59)

    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
    start_date = date_obj - datetime.timedelta(days=90)
    start_date = datetime.datetime(start_date.year, start_date.month, start_date.day, hour=0, minute=0, second=0)
    reports_logger.info("Фильтрация операций по категории")
    filtered_data = transactions.loc[
        (transactions["Дата операции"] >= start_date)
        & (transactions["Дата операции"] <= date_obj)
        & (transactions["Категория"] == category)
    ]

    return filtered_data
