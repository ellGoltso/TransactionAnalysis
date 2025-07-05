import datetime

from src.reports import spending_by_category
from src.services import get_json_transfers_data
from src.utils import get_df_data
from src.views import get_json_data

date_t = datetime.datetime(2021, 12, 16, 16, 27, 0)
print(get_json_data(date_t))
spending_by_category(get_df_data(), "Супермаркеты", "17.12.2021")
print(get_json_transfers_data())
