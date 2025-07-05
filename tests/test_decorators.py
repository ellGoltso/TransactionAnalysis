import datetime
import json

import pandas as pd

from src.decorators import write_to_file


def test_write_to_file():
    @write_to_file("data/test_data.json")
    def test_func():
        return pd.DataFrame({"Column_1": [1, 2, 3, 4, 5], "Column_2": [5, 4, 3, 2, 1]})

    test_func()

    with open("data/test_data.json", "r", encoding="utf-8") as f:
        content = json.load(f)

    pd.testing.assert_frame_equal(
        pd.DataFrame(content), pd.DataFrame({"Column_1": [1, 2, 3, 4, 5], "Column_2": [5, 4, 3, 2, 1]})
    )

    @write_to_file("data/test_exc.json")
    def test_exc():
        return datetime.datetime(2024, 12, 2, 13, 2, 23)

    test_exc()

    with open("data/test_exc.json", "r", encoding="utf-8") as f:
        content = json.load(f)

    assert content == "test_exc error: 'datetime.datetime' object has no attribute 'to_json'."
