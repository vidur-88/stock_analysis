from datetime import datetime

from init_celery import app
from utils.nifty_index_stocks_price_data import get_nifty_index_stocks_data
from utils.capture_data import write_data_to_file


@app.task(name="nifty_index_stock_data_capturing")
def nifty_index_stock_data_capturing(nifty_index_name):
    try:
        print("Receive celery task to write, index_name: {}".format(nifty_index_name))
        stocks_data = get_nifty_index_stocks_data(nifty_index_name)
        time_stamp = stocks_data.get("time_stamp", datetime.now())
        for stock_symbol, data in stocks_data.items():
            if stock_symbol == "time_stamp":
                continue

            store_data_to_file.delay("nifty_stock", nifty_index_name, stock_symbol, str(time_stamp), data)
    except Exception as e:
        print("Error, msg: {}".format(e.args))


@app.task(name="store_data_to_file")
def store_data_to_file(data_type, nifty_index_name, stock_symbol, time_stamp, data):
    try:
        write_data_to_file(data_type, nifty_index_name, stock_symbol, time_stamp, data)
    except Exception as e:
        print("Error, msg: {}".format(e.args))


# if __name__ == "__main__":
#     nifty_index_name = "NIFTY 50"
#     stocks_data = get_nifty_index_stocks_data(nifty_index_name)
#     time_stamp = stocks_data.get("time_stamp", datetime.now())
#     for stock_symbol, data in stocks_data.items():
#         if stock_symbol == "time_stamp":
#             continue
#
#         store_data_to_file("nifty_stock", nifty_index_name, stock_symbol, str(time_stamp), data)