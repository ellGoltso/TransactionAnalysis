import datetime

import pandas as pd



def get_data_from_excel_file(date):
    """  """

    excel_data = pd.read_excel("data/operations.xlsx")
    excel_data['Дата операции'] = pd.to_datetime(excel_data['Дата операции'])
    end_date = datetime.datetime(date.year, date.month, date.day, 23, 59, 59)
    start_date = datetime.datetime(date.year, date.month, 1)
    filtered_data = excel_data.loc[(excel_data['Дата операции'] >= start_date) & (excel_data['Дата операции'] <= end_date)]

    # print(filtered_data)


# date = datetime.datetime(2021, 12, 4)
# get_data_from_excel_file(date)
