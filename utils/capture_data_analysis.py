from datetime import date, timedelta
from pathlib import Path

import pandas as pd

base_path = "/var/log/capture_data/data_{}/{}"


def read_capture_data_for_date(date_to_read, data_type, index_name=""):
    file_parent_path = base_path.format(date_to_read, data_type+ "_" + index_name)
    file_list = [fl for fl in Path(file_parent_path).iterdir() if fl.is_file()]
    for file_name in file_list:
        print(file_name)
        df = pd.read_csv(file_name)
        if "symbol" in df.columns:
            yield df, df[["symbol"]].values[0][0]
        else:
            yield df, df[["indexName"]].values[0][0]


def read_capture_data_in_range(from_date, to_date, data_type, index_name=""):
    n_days = int((to_date - from_date).days)
    for n in range(n_days):
        date_to_read = from_date + timedelta(n)
        date_to_read = date_to_read.strftime("%Y_%m_%d")
        stock_data = read_capture_data_for_date(date_to_read, data_type, index_name)
        for sd in stock_data:
            yield sd


if __name__ == "__main__":
    date1 = date.today() - timedelta(5)
    date2 = date1 + timedelta(4)
    dd = read_capture_data_in_range(date1, date2, "nifty_stock", "NIFTY 50")
    result = {}
    for sd, symbol in dd:
        if symbol == "NIFTY 50":
            result[symbol] = sd[["ltp", "high", "low", "yHigh", "yLow", "time_stamp"]].to_dict("records")
            print(sd[["ltp", "high", "low", "yHigh", "yLow", "time_stamp"]].to_dict("records"), symbol)
        else:
            result[symbol] = sd[["ltP", "high", "low", "wkhi", "wklo", "open", "previousClose", "dayEndClose", "trdVolM", "time_stamp"]].to_dict("records")
            print(sd[["ltP", "high", "low", "wkhi", "wklo", "open", "previousClose", "dayEndClose", "trdVolM", "time_stamp"]].to_dict("records"), symbol)
