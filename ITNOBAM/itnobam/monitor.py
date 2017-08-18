#!/usr/bin/python3
# -*- coding: utf-8 -*-
# monitor.py 
#
# module to handle the sensors and monitoring of users world

import itnobam_config as config

def main():
    """
    main function used for testing 
    """
    s = Sensors()
    s.scan()
    return s.which_room_am_i_in()

    
    
class Sensors:
    def scan(self):
        """
        scan all sensors
        """
        
        for area in config.areas:
            #print('area = ',area)
            #print('area = ',area[sensor_id])
            #print('k,v = ', k,v)
            for k,v in area.items():
                if k == 'sensor_id':
                    print('scanning ' + v)
            
        return 'TODO'

    def which_room_am_i_in(self):
        return 'Bedroom'

    
if __name__ == '__main__':
    main()