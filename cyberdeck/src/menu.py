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
    main_menu_loop()

def main_menu_loop():
    current_menu = 'ROOT'
    conn = sqlite3.connect(utils.db_file)
    menu_sql = 'SELECT id, parent_id, menu_id, sort_order,menu_text,help_text FROM p_menu'
    res = utils.get_data(conn, menu_sql, [])
    #for row in res:
    #    print(row)

    if verify_data(res) == False:
        print('Error - data for menu is not valid')
        quit()

    while current_menu != 'EXIT':
        for row in res:
            if row[1] == current_menu:
                display_menu_row(row)
        print('99 = Back to root menu')            
        x = input('Enter menu > ')
        if x == '':
            quit()
        if x == '99':
            current_menu = 'ROOT'
        else:
            sel_row = get_selected_row_for_menu(res, x)
            selected_option = sel_row[2]
            selected_parent = sel_row[1]
            #print(selected_option)
            current_menu = selected_option
            if selected_parent != 'ROOT':
                print('running command : ' + str(current_menu))
            else:
                print(' --- ' + sel_row[2] + ' ---')

def display_menu_row(rw):
    """
    currently prints to screen but likely to go to LCD 80x4 via I2C
    """
    print(str(rw[0]) + ' = ' + str(rw[4]))

def get_selected_row_for_menu(rows, menu_num):
    for row in rows:
        if int(menu_num) == row[0]:
            #print(' found row : ' + str(row))
            return row
    print(' cant find menu_item' + str(menu_num))
    return [0,0,'unk_menu', 'unk_parent', 0, 'Unk','Unk']

def verify_data(res):
    tok = True
    all_parent_menus = []
    for r in res:
        if r[0] not in all_parent_menus:
            all_parent_menus.append(r[0])

    for r2 in res:
        if r2[0] not in all_parent_menus:
                print(str(r2) + ' not in parent menu : ' + str(all_parent_menus) )
                tok = False

    return tok

def quit():
    print('Bye!')
    sys.exit()


if __name__ == '__main__':
    main()
        