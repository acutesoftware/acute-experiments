#!/usr/bin/python3
# -*- coding: utf-8 -*-
# z_setup_folders.py 

import os 
import sys 
import sqlite3

sys.path.append(r"C:\C_DATA\dev\src\procgen\src\genCode")
import if_sqllite

db_file = r'C:\C_DATA\dev\src\acute_experiment\cyberdeck\data\buildr.db'


def_lp_tables = [ # [table_name, description, grain_cols, col_list, cols_INT, cols_REAL, cols_BLOB]
    # CREATED AUTOMATICALLY ['s_filelist_raw', 'List of Raw files', 'fullFilename', 'fullFilename, name, path, size, date, dummy', ['size'], [], []],
    ['o_part_types', 'Part types', 'part_type_desc', 'part_type_desc', [], [], []],

]

def_lp_jobs = [ # proj_id, job_num, job_id, details
    ['DAT', 1, 'LOAD_DATA', 'Loads Data from CSV'],
]


def_lp_job_steps = [ # job_id, job_num, step_num, job_type, details, sql_to_run
    

    [ 'LOAD_DATA', 0, 1, 'CSV', r'C:\C_DATA\dev\src\acute_experiment\cyberdeck\data\p_menu.csv', '', 'Load ref file CSV files into own tables', '', ''],

]


def main():
    print("Setup structure for development")
    if os.path.exists(db_file):
        print('ERROR - database already setup. Everything will be wiped if you continue - delete database manually first')
        print('To WIPE the database and rebuild type GO and press enter, otherwise - press Enter to cancel')
        x = input()
        if x != 'GO':
            sys.exit()

    try:
        os.remove(db_file)
    except Exception as ex:
        if '[WinError 32]' in str(ex):
            print('Whoops - you left the database open - ' + str(ex))
            sys.exit()
        pass
    if_sqllite.create_database(db_file)
    conn = sqlite3.connect(db_file)
    setup_tables(conn)
    define_jobs(conn)
    run_etl(conn)
    populate_sample_prod_data(conn)
    print('Done!')   

def setup_tables(conn):
    if_sqllite.init_metadata_tables(conn)  # defines the table definitions

    for tbl in def_lp_tables:
        if_sqllite.create_table_from_definition(conn, tbl)


def define_jobs(conn):
    if_sqllite.lg(conn, if_sqllite.LOG_DATA, 'defining jobs')
    for job in def_lp_jobs:
        if_sqllite.job_create(conn, job[0], job[1], job[2], job[3])

    for step in def_lp_job_steps:  # job_id, step_num, job_type, src_tbl, dest_tbl, details, sql_to_run
        #print('adding step = ' + str(step))
        if_sqllite.job_add_step(conn, step[0],step[1],step[2],step[3],step[4], step[5], step[6], step[7], step[8])

def run_etl(conn):
    if_sqllite.lg(conn, if_sqllite.LOG_DATA, 'running ETL jobs')

    if_sqllite.run_all_jobs(conn)

def populate_sample_prod_data(conn):
    sql = []

    sql.append("INSERT INTO o_part_types (part_type_desc) VALUES ('Electronic')")
    sql.append("INSERT INTO o_part_types (part_type_desc) VALUES ('Metal')")
    sql.append("INSERT INTO o_part_types (part_type_desc) VALUES ('Misc')")
    sql.append("INSERT INTO o_part_types (part_type_desc) VALUES ('Software')")
    sql.append("INSERT INTO o_part_types (part_type_desc) VALUES ('Service')")
  

    # now run all the SQL commands
    for s_num, s in enumerate(sql):
        step = [ 'CAL', 3, 10+s_num, 'UPD', '', 'misc', 'adding data', s, '']
        if_sqllite.job_add_step(conn, step[0],step[1],step[2],step[3],step[4], step[5], step[6], step[7], step[8])
        if_sqllite.run_job_step(conn, step)



if __name__ == '__main__':
    main()
    