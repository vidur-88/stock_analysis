import os
import csv

curr_dir = os.getcwd()
SYMBOL_LIST_FILE_NAME = curr_dir + '/nse_symbol_list.txt'
SECTOR_SYMBOL_LIST_FILE_NAME = curr_dir + '/EQUITY_L.csv'


def get_symbols():
    symbols = list()

    for line in file(SYMBOL_LIST_FILE_NAME, 'r'):
        symbols.append(line.strip())

    return symbols


def get_sector_symbols(sector):
    symbols = list()

    with open(SECTOR_SYMBOL_LIST_FILE_NAME) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row['SECTOR'].upper() == sector:
                symbols.append(row['SYMBOL'].strip())

    return symbols
