import sys
import datetime

from src.reports import spending_by_category
from src.utils import get_df_data
from src.views import get_json_data

# print(sys.path)
# date_t = datetime.datetime(2021, 12, 16, 16, 27, 0)
# get_json_data(date_t)
print(spending_by_category(get_df_data(), 'Супермаркеты', '17.12.2021'))