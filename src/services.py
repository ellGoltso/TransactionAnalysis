import logging
import re

from src.utils import get_df_data

services_logger = logging.getLogger("services")
file_handler = logging.FileHandler("logs/services.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
services_logger.addHandler(file_handler)
services_logger.setLevel(logging.DEBUG)

pattern = re.compile(r"^\b\D+\b \D\.$")


def get_json_transfers_data():
    """Возвращает json с транзакциями, которые относятся к переводам физлицам"""

    data = get_df_data()
    services_logger.info("Фильтрация транзакций, относящихся к переводам физ.лицам")
    transfers = data.loc[(data["Категория"] == "Переводы") & (data["Описание"].str.contains(pattern))]
    json_data = transfers.to_json(orient="records", force_ascii=False, indent=4)
    return json_data
