#!/usr/bin/python3
# -*- coding: utf-8 -*-
# utils.py 

import os 
import sys 
import sqlite3

db_file = r'C:\C_DATA\dev\src\acute_experiment\cyberdeck\data\buildr.db'


def get_data(conn, sql, param):
    """
    runs SQL against a db - used for everything.
    No, there is no SQL injection tests because it is single user.
    """
    #lg(LOG_INFO, 'running SQL ' + sql)
    try:
        c = conn.cursor()
        #print('get_data - sql = ' + sql + ' , param = ' + str(param))
        c.execute(sql, param)
        rows = c.fetchall()
        return rows

    except Exception as e:
        lg(conn, LOG_ERROR, 'Error getting data ' + str(e))    
