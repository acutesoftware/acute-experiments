#!/usr/bin/python3
# -*- coding: utf-8 -*-
# z_setup_folders.py 

import os 
import sys 
import sqlite3
import if_sqllite

data_folder = r'/home/duncan/dev/src/python/acute-experiments/cyberdeck/data'
src_folder = r'/home/duncan/dev/src/python/acute-experiments/cyberdeck/src'


db_file = os.path.join(data_folder, 'buildr.db')


def_lp_tables = [ # [table_name, description, grain_cols, col_list, cols_INT, cols_REAL, cols_BLOB]
    ['o_part_types', 'Part types', 'part_type_desc', 'part_type_desc', [], [], []],
    #    ['o_parts', 'Parts', 'nme,part_type_id,dsc,quant', 'nme', ['quant'], [], []],
]

def_lp_jobs = [ # proj_id, job_num, job_id, details
    ['DAT', 1, 'LOAD_DATA', 'Loads Data from CSV'],
]


def_lp_job_steps = [ # job_id, job_num, step_num, job_type, details, sql_to_run
    
    [ 'LOAD_DATA', 0, 1, 'CSV', os.path.join(data_folder, 'p_menu.csv'), '', 'Load ref file CSV files into own tables', '', ''],
    [ 'LOAD_DATA', 0, 2, 'CSV', os.path.join(data_folder, 'o_interface.csv'), '', 'Load ref file CSV files into own tables', '', ''],
    [ 'LOAD_DATA', 0, 3, 'CSV', os.path.join(data_folder, 'o_parts.csv'), '', 'Load ref file CSV files into own tables', '', ''],
    [ 'LOAD_DATA', 0, 4, 'CSV', os.path.join(data_folder, 'o_feature.csv'), '', 'Load ref file CSV files into own tables', '', ''],
    [ 'LOAD_DATA', 0, 5, 'CSV', os.path.join(data_folder, 'f_feature_interface.csv'), '', 'Load ref file CSV files into own tables', '', ''],

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
        print('Whoops - you may have left the database open - ' + str(ex))
        sys.exit()

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
    sql.append("INSERT INTO o_part_types (part_type_desc) VALUES ('External')")
  

    sql.append("""CREATE VIEW u_parts AS
select tp.part_type_desc, prt.nme, prt.dsc, prt.quant 
from o_parts prt, o_part_types tp
where prt.part_type_id = tp.id               
""")

    sql.append("""CREATE VIEW u_menu AS
select id, menu_id, parent_id, sort_order, menu_text, help_text,
'fn_' || menu_id || '.py' as script_name,
'from ' || lower(parent_id) || ' import fn_' || menu_id || ' as mod_' || lower(menu_id) as script_import,
'/home/duncan/dev/src/python/acute-experiments/cyberdeck/src/' || lower(menu_id) || '/' as script_folder
 from p_menu
""")


    # now run all the SQL commands
    for s_num, s in enumerate(sql):
        step = [ 'CAL', 3, 10+s_num, 'UPD', '', 'misc', 'adding data', s, '']
        if_sqllite.job_add_step(conn, step[0],step[1],step[2],step[3],step[4], step[5], step[6], step[7], step[8])
        if_sqllite.run_job_step(conn, step)



if __name__ == '__main__':
    main()
    
