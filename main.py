import sys
import datetime
from src.views import get_json_data

# print(sys.path)
date_t = datetime.datetime(2021, 12, 16, 16, 27, 0)
get_json_data(date_t)