import datetime
from unittest.mock import patch

import pandas as pd
import pytest

from src.utils import get_data_from_excel_file, get_general_information, get_greetings, get_top_five_transactions


@pytest.mark.parametrize(
    "x, expected",
    [
        (datetime.datetime(2025, 7, 1, 7, 30, 0), "Доброе утро"),
        (datetime.datetime(2025, 7, 1, 15, 30, 0), "Добрый день"),
        (datetime.datetime(2025, 7, 1, 19, 30, 0), "Добрый вечер"),
        (datetime.datetime(2025, 7, 1, 3, 30, 0), "Доброй ночи"),
    ],
)
def test_greetings(x, expected):
    assert get_greetings(x) == expected


@patch("pandas.read_excel")
def test_data_from_excel_file(mock_get, fixture_df_data):

    mock_get.return_value = fixture_df_data
    data = get_data_from_excel_file(datetime.datetime(2021, 12, 14))
    pd.testing.assert_frame_equal(data, fixture_df_data)


def test_get_general_information(fixture_df_data):

    expected_data = [{"last_digits": "*7197", "total_spent": 309.0, "cashback": round(309.0 / 100, 2)}]
    assert expected_data == get_general_information(fixture_df_data)


def test_get_top_five(fixture_df_data):

    fixture_df_data["Дата операции"] = pd.to_datetime(fixture_df_data["Дата операции"], dayfirst=True)
    expected_data = [
        {
            "Дата операции": "14.12.2021",
            "Сумма операции с округлением": 309.0,
            "Категория": "Супермаркеты",
            "Описание": "Колхоз",
        }
    ]

    assert expected_data == get_top_five_transactions(fixture_df_data)
