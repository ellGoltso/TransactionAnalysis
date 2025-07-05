from src.utils import get_df_data


def get_json_transfers_data():
    """Возвращает json с транзакциями, которые относятся к переводам физлицам"""

    data = get_df_data()
    transfers = data.loc[
        (data["Категория"] == "Переводы") & (data["Описание"].str.contains(r"^\b\D+\b \D\.$", regex=True))
    ]
    json_data = transfers.to_json(orient="records", force_ascii=False)
    return json_data
