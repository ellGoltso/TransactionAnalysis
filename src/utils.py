import datetime
import logging

import pandas as pd

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_greetings(date: datetime.datetime) -> str:
    """Принимает дату и время и возвращает строку приветствия в зависимости от времени суток"""

    greeting = ""
    utils_logger.info("Определяется формат приветствия")
    if 5 <= date.hour < 12:
        greeting = "Доброе утро"
    elif 12 <= date.hour < 16:
        greeting = "Добрый день"
    elif 16 <= date.hour < 24:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    return greeting


def get_df_data(path: str = "data/operations.xlsx") -> pd.DataFrame:
    """Опционально принимает путь к excel файлу и возвращает DataFrame с данными"""

    try:
        utils_logger.info("Считывание данных из файла")
        excel_data = pd.read_excel(path)
    except FileNotFoundError:
        utils_logger.error("Файл не найден")
        return pd.DataFrame()

    return excel_data


def get_data_from_excel_file(date: datetime.datetime) -> pd.DataFrame:
    """Принимает дату и возвращает DataFrame с операциями с начала месяца до указанной даты"""

    excel_data = get_df_data()
    excel_data["Дата операции"] = pd.to_datetime(excel_data["Дата операции"], dayfirst=True)
    end_date = datetime.datetime(date.year, date.month, date.day, 23, 59, 59)
    start_date = datetime.datetime(date.year, date.month, 1)
    utils_logger.info("Фильтрация данных")
    filtered_data = excel_data.loc[
        (excel_data["Дата операции"] >= start_date) & (excel_data["Дата операции"] <= end_date)
    ]

    return filtered_data


def get_general_information(data: pd.DataFrame) -> list[dict]:
    """Принимает DataFrame, группирует по номеру карты и
    возвращает список словарей с информацией по каждой карте"""

    data["Номер карты"] = data["Номер карты"].fillna("missing")
    grouped_data = data.groupby("Номер карты")
    sum_operations_by_card = grouped_data["Сумма операции с округлением"].sum().reset_index()
    sum_operations_by_card["Сумма операции с округлением"] = sum_operations_by_card[
        "Сумма операции с округлением"
    ].astype(float)
    card_numbers: list = sum_operations_by_card["Номер карты"].tolist()
    sums_list: list = sum_operations_by_card["Сумма операции с округлением"].tolist()
    info_list: list = []
    utils_logger.info("Группировка данных по номеру карты")
    for index, value in enumerate(card_numbers):
        info_dict = {
            "last_digits": value,
            "total_spent": round(sums_list[index], 2),
            "cashback": round(sums_list[index] / 100, 2),
        }
        info_list.append(info_dict)

    return info_list


def get_top_five_transactions(data: pd.DataFrame) -> list[dict]:
    """Принимает DataFrame с операциями и возвращает список словарей с топ 5 операциями по сумме"""

    utils_logger.info("Сортировка DataFrame")
    sorted_data = data.sort_values(by="Сумма операции с округлением", ascending=False)
    selected_columns = ["Дата операции", "Категория", "Описание", "Сумма операции с округлением"]
    slice_of_values = sorted_data[selected_columns].iloc[:5]
    slice_of_values["Дата операции"] = slice_of_values["Дата операции"].apply(
        lambda x: datetime.date(x.year, x.month, x.day)
    )
    operations = slice_of_values.to_dict("records")
    for i in operations:
        i["Дата операции"] = i["Дата операции"].strftime("%d.%m.%Y")

    return operations
