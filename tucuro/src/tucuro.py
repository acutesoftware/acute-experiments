#!/usr/bin/python3
# coding: utf-8
# tucuro.py

import os
import json 

def main():
    interface_list = [d for d in os.listdir('interface') if os.path.isdir(os.path.join('interface',d))]
    for interface in interface_list:
        import_game_data(interface)


def import_game_data(interface):
    """
    imports stats to standard format using definitions
    in 'interface' folder
    """
    try:
        with open(os.path.join('interface', interface, 'map.json')) as f:
            print('importing stats from ' + interface)
            res = json.loads(f.read())
            read_game_stats(res)
    except Exception as ex:
        print('no mapping file defined for ' + interface + str(ex))

def read_game_stats(json_data):
    print(json.dumps(json_data))
    print(json_data["name"])


if __name__ == "__main__":
    main()