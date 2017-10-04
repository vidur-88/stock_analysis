import os


def get_symbols_list():
    symbols = list()

    symbol_list_file_name = os.getcwd() + '/nse_symbol_list.txt'
    for line in file(symbol_list_file_name, 'r'):
        symbols.append(line.strip())

    return symbols
