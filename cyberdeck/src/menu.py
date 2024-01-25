#!/usr/bin/python3
# -*- coding: utf-8 -*-
# menu.py 
# written by Duncan Murray 24/1/2024
# This is the main menu to be run on the cyberdeck
import sqlite3
import utils

def main():
    print('WELCOME TO CYBERDECK')
    current_menu = 'ROOT'
    conn = sqlite3.connect(utils.db_file)
    menu_sql = 'SELECT parent_id, menu_id FROM p_menu'
    res = utils.get_data(conn, menu_sql, [])
    for row_num, row in enumerate(res):
        if row[0] == current_menu:
            print(str(row_num) + ' = ' + row[1])


if __name__ == '__main__':
    main()
        