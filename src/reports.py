import datetime
from typing import Optional

import pandas as pd

from src.decorators import write_to_file


@write_to_file()
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция принимает на вход:
        датафрейм с транзакциями,
        название категории,
        опциональную дату.
    Если дата не передана, то берется текущая дата.
    Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)"""

    if date is None:
        date_obj = datetime.date.today()
    else:
        date_obj = datetime.datetime.strptime(date, "%d.%m.%Y")
    date_obj = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, hour=23, minute=59, second=59)

    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
    start_date = date_obj - datetime.timedelta(days=90)
    start_date = datetime.datetime(start_date.year, start_date.month, start_date.day, hour=0, minute=0, second=0)
    filtered_data = transactions.loc[
        (transactions["Дата операции"] >= start_date)
        & (transactions["Дата операции"] <= date_obj)
        & (transactions["Категория"] == category)
    ]

    return filtered_data
