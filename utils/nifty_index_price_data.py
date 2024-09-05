import pandas as pd

from utils.parse_panda_dict import parse_panda_to_dict


URL = "https://iislliveblob.niftyindices.com/jsonfiles/LiveIndicesWatch.json"


def get_nifty_indices_data():
    nifty_url = URL
    df = pd.read_json(nifty_url)
    df = parse_panda_to_dict(df)
    return df


def get_nifty_index_to_data():
    indices_data = get_nifty_indices_data().get("data")
    result = {}
    for index_data in indices_data:
        if len(index_data) > 0:
            for _, i_data in index_data.items():
                result.setdefault(i_data["indexName"], []).append(i_data)
    return result


if __name__ == "__main__":
    indices_data = get_nifty_index_to_data()
    print(indices_data.keys())
    print(indices_data)