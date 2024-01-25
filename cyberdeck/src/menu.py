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
    menu_sql = 'SELECT parent_id, menu_id, sort_order,menu_text,help_text FROM p_menu'
    res = utils.get_data(conn, menu_sql, [])

    while current_menu != 'EXIT':
        for row_num, row in enumerate(res):
            if row[0] == current_menu:
                print(row[1] + ' = ' + row[3])
        x = input('Enter menu > ')
        current_menu = x.upper()
        #if current_menu



if __name__ == '__main__':
    main()
        