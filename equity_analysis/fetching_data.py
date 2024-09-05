import itertools
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
import numpy as np
from nsepy.history import get_history, get_history_quanta


class FetchingData():
    def __init__(self, params):
        self.exchange = params['exchange']
        self.symbol = params['symbol']
        self.to_date = params.get('to_date')
        self.from_date = params.get('from_date')
        self.num_of_months = params.get('num_of_months')
        self.num_of_days = params.get('num_of_days')
        self.set_time_period()

    def get_data(self):
        history_data = self.__fetch_data()
        return self.__parse_data(history_data)

    def get_time_interval(self):
        return self.from_date, self.to_date

    def set_time_period(self):
        if not self.from_date and not self.to_date and \
                not self.num_of_days and not self.num_of_months:
            self.to_date = date.today()
            self.from_date = self.to_date + relativedelta(years=-1)
        elif self.from_date and not self.to_date:
            self.from_date = datetime.strptime(self.from_date, "%Y-%m-%d").date()
            self.to_date = date.today()
        elif not self.from_date:
            if self.num_of_days:
                self.to_date = date.today()
                self.from_date = self.to_date + relativedelta(days=-self.num_of_days)
            elif self.num_of_months:
                self.to_date = date.today()
                self.from_date = self.to_date + relativedelta(months=-self.num_of_months)
        elif self.from_date and self.to_date:
            self.from_date = datetime.strptime(self.from_date,
                                               "%Y-%m-%d").date()
            self.to_date = datetime.strptime(self.to_date,
                                             "%Y-%m-%d").date()

    def __fetch_data(self):
        history_data = get_history(symbol=self.symbol,
                                   start=self.from_date,
                                   end=self.to_date)
        # Date index is string type so we can't add freq
        # So, need to make Datetime index and add freq 1-Day
        #
        history_data = history_data.reset_index()
        history_data['Date'] = pd.to_datetime(history_data['Date'])
        history_data = history_data.set_index('Date')
        history_data = history_data.resample('1D').mean()
        return history_data

    def __parse_data(self, history_data):
        columns = list(history_data)
        resp = dict()
        for column in columns:
            data = history_data[column]
            data = data.fillna(data.bfill())
            resp[column] = data

        for col in resp:
            date_col = list(resp[col].index)
            data_col = list(resp[col])
            resp[col] = list()
            for x, y in itertools.zip_longest(date_col, data_col):
                x = x.strftime('%Y-%m-%d')
                resp[col].append({x: y})
        return resp


if __name__ == '__main__':
    params = {'exchange': 'NSE', 'symbol': 'PNB', 'num_of_months': 2}
    print(len(FetchingData(params).get_data()['Close']))
