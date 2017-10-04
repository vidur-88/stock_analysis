from equity_analysis.fetching_data import FetchingData
from equity_analysis.utils import get_symbols_list


class CompanyData(object):
    def __init__(self):
        pass

    def get_company_data(self, params):
        return FetchingData(params).get_data()


class AllCompanyData(CompanyData):
    def __init__(self, params):
        super(AllCompanyData, self).__init__()
        self.params = params

    def get_all_company_data(self):
        symbols = get_symbols_list()
        resp = dict()

        for symbol in symbols:
            self.params['symbol'] = symbol
            resp[symbol] = self.get_company_data(self.params)

        return resp
