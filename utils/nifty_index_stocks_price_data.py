from datetime import datetime
import requests

import pandas as pd

from utils.parse_panda_dict import parse_panda_to_dict


URL = "https://iislliveblob.niftyindices.com/jsonfiles/equitystockwatch/EquityStockWatch{}.json"


def get_nifty_index_data(nifty_index_name):
    nifty_index_name = nifty_index_name.replace(" ", "%20")
    nifty_url = URL.format(nifty_index_name)
    resp = requests.get(nifty_url, headers={"Content-Type": "application/json", "Accept": "application/json"})
    df = pd.json_normalize(resp.json())
    df = parse_panda_to_dict(df)
    return df


def get_nifty_index_stocks_data(nifty_index_name):
    nifty_index_stock_info = get_nifty_index_data(nifty_index_name)
    nifty_index_stock_data = nifty_index_stock_info.get("data")
    nifty_index_data = nifty_index_stock_info.get("latestData")
    nifty_time = nifty_index_stock_info.get("time")
    result = {}

    if nifty_index_stock_data and nifty_index_stock_data[0]:
        for _, stock_data in enumerate(nifty_index_stock_data[0][0]):
            result[stock_data["symbol"]] = stock_data

    if nifty_index_data and nifty_index_data[0]:
        for _, index_data in enumerate(nifty_index_data[0][0]):
            result[index_data["indexName"]] = index_data

    if nifty_time and nifty_time[0]:
        result["time_stamp"] = datetime.strptime(nifty_time[0][0], "%b %d, %Y %H:%M:%S")
    return result


if __name__ == "__main__":
    index_data = get_nifty_index_stocks_data("NIFTY 50")
    print(index_data.keys())
    print(index_data)