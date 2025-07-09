import json

import pandas as pd

from src.reports import spending_by_category


def test_spending_by_category(fixture_df_data):
    spending_by_category(fixture_df_data, "Супермаркеты", "14.02.2022")

    with open("data/function_results.json", "r", encoding="utf-8") as f:
        content = json.load(f)
    print(content)

    data = pd.DataFrame(content)
    data["Дата операции"] = pd.to_datetime(data["Дата операции"], dayfirst=False)
    pd.testing.assert_frame_equal(data, fixture_df_data)
