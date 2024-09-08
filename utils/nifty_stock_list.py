from collections import defaultdict
import pandas as pd

from utils.parse_panda_dict import parse_panda_to_dict


URL = "https://iislliveblob.niftyindices.com/jsonfiles/HeatmapDetail/FinalHeatmapNIFTY%20{}.json"


def get_nifty_data(nifty_type):
    nifty_url = URL.format(nifty_type)
    df = pd.read_json(nifty_url)
    # df = df.reset_index()
    # df['Date'] = pd.to_datetime(datetime.now())
    # df = df.set_index('Date')
    # df = df.resample('1D')
    df = parse_panda_to_dict(df)
    return df


def get_nifty_symbol_sector(nifty_data):
    symbols = nifty_data['symbol']
    sectors = nifty_data['sector']
    sector_wise_symbol = defaultdict(list)
    for idx_sec in sectors:
        for idx, sec in idx_sec.items():
            for idx_sym in symbols:
                for id, sym in idx_sym.items():
                    if id == idx:
                        sector_wise_symbol[sec].append(sym)
                        break

    return sector_wise_symbol


if __name__ == "__main__":
    nifty_data = get_nifty_data("TOTAL%20MARKET")
    nifty_sector_symbol = get_nifty_symbol_sector(nifty_data)
    total_sym = 0
    for sec, sym in nifty_sector_symbol.items():
        total_sym += len(sym)
        print(sec, sym)

    print(total_sym)