import itertools


def parse_panda_to_dict(h_data):
    columns = h_data.columns
    resp = dict()
    for column in columns:
        data = h_data[column]
        data = data.fillna(data.bfill())
        resp[column] = data

    for col in resp:
        date_col = list(resp[col].index)
        data_col = list(resp[col])
        resp[col] = list()
        for x, y in itertools.zip_longest(date_col, data_col):
            resp[col].append({x: y})
    return resp