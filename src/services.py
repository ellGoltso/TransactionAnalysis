import json
import re


import pandas as pd


def get_data():
    """  """

    data = pd.read_excel("data/operations.xlsx")
    transfers = data.loc[(data['Категория'] == 'Переводы') & (data['Описание'].str.contains(r'^\b\D+\b \D\.$', regex = True))]
    json_data = transfers.to_json(orient='records', force_ascii = False)
    return json_data
