#!/usr/bin/python3
# coding: utf-8
# tucuro.py

import os


def main():
    interface_list = [d for d in os.listdir('interface') if os.path.isdir(os.path.join('interface',d))]
    for interface in interface_list:
        print('import stats from ' + interface)


def import_stats(game):
    """
    imports stats to standard format using definitions
    in 'interface' folder
    """




if __name__ == "__main__":
    main()