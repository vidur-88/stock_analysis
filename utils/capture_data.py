from datetime import date
from pathlib import Path

import pandas as pd

base_path = "/var/log/capture_data/data_{}/{}"


def write_data_to_file(data_type, nifty_index_name, stock_symbol, time_stamp, data):
    today_date = date.today().strftime("%Y_%m_%d")
    last_folder_name = data_type
    if stock_symbol:
        last_folder_name = "{}_{}".format(data_type, nifty_index_name)
    path_name = base_path.format(today_date, last_folder_name)

    Path(path_name).mkdir(parents=True, exist_ok=True)
    file_path = "{}/{}.csv".format(path_name, stock_symbol if stock_symbol else nifty_index_name)
    write_data(file_path, data, time_stamp)


def write_data(file_path, data, time_stamp):
    data["time_stamp"] = time_stamp
    df = pd.DataFrame([data.values()], columns=data.keys())
    df.to_csv(file_path, mode="a", header=False if Path(file_path).is_file() else True)


