#!/usr/bin/python3
# -*- coding: utf-8 -*-
# z_setup_folders.py 

import os 
import sys 
import sqlite3

sys.path.append(r"C:\C_DATA\dev\src\procgen\src\genCode")
import utils

base_folder = r'C:\C_DATA\dev\src\acute_experiment\cyberdeck\src'


prog_template = """
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ###PROGNAME###.py 

def main():
    print('Running ###PROGNAME###')

    
if __name__ == '__main__':
    main()
 

"""

def main():
    print("Setup folders for development")
    conn = sqlite3.connect(utils.db_file)
    menu_sql = 'SELECT parent_id, menu_id FROM p_menu'
    res = utils.get_data(conn, menu_sql, [])

    # make root folders and add a library for that area
    for row in res:
        if row[0] == 'ROOT':
            fldr = base_folder + os.sep + row[1].lower()
            if row[1] != 'EXIT':
                print('Creating root folder : ' + fldr)
                os.makedirs(fldr, exist_ok=True)

    # make full list of programs and put them in appropriate folders- ONLY IF THEY DONT EXIST
    for row in res:
        if row[0] != 'ROOT' and row[1] != 'ROOT':
            fldr = base_folder + os.sep + row[0].lower()
            prog = 'fn_' + row[1].lower() + '.py'
            fullname = fldr + os.sep + prog
            if os.path.exists(fullname):
                print('WARNING - file already exists, not overwriting : ' + fullname)
            else:
                print('Creating program template : ' + fullname )
                code = prog_template.replace('###PROGNAME###', row[1].lower())
                with open(fullname, 'w' ) as fop:
                    fop.write(code)


if __name__ == '__main__':
    main()
    