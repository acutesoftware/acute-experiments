#!/usr/bin/python3
# -*- coding: utf-8 -*-
# menu.py 
# written by Duncan Murray 24/1/2024
# This is the main menu to be run on the cyberdeck
import sqlite3
import utils
import sys

def main():
    print('WELCOME TO CYBERDECK')
    current_menu = 'ROOT'
    conn = sqlite3.connect(utils.db_file)
    menu_sql = 'SELECT parent_id, menu_id, sort_order,menu_text,help_text FROM p_menu'
    res = utils.get_data(conn, menu_sql, [])

    while current_menu != 'EXIT':
        for row_num, row in enumerate(res):
            if row[0] == current_menu:
                print(str(row_num) + ' = ' + row[3])
        print('99 = Back to root menu')            
        x = input('Enter menu > ')
        if x == '':
            sys.exit()
        if x == '99':
            current_menu = 'ROOT'
        else:
            selected_option = res[int(x)][1]
            selected_parent = res[int(x)][0]
            print(selected_option)
            current_menu = selected_option
            if selected_parent != 'ROOT':
                print('running command : ' + current_menu)



if __name__ == '__main__':
    main()
        