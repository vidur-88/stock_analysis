from equity_analysis.fetching_data import FetchingData
from equity_analysis.utils import get_symbols, get_sector_symbols


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
        symbols = get_symbols()
        resp = dict()

        for symbol in symbols:
            self.params['symbol'] = symbol
            resp[symbol] = self.get_company_data(self.params)

        return resp


class SectorWiseData(CompanyData):
    def __init__(self, params):
        super(SectorWiseData, self).__init__()
        self.params = params

    def get_companies_data(self):
        symbols = get_sector_symbols(self.params['sector'].upper())
        resp = dict()

        for symbol in symbols:
            self.params['symbol'] = symbol
            resp[symbol] = self.get_company_data(self.params)

        return resp
