#!/usr/bin/python3
# -*- coding: utf-8 -*-
# main_robot_loop.py 

import time
import random

sensors = [
            {'name':'light', 'value':-1},
            {'name':'sound', 'value':-1},
            {'name':'distance_front', 'value':-1},
            {'name':'distance_front_left', 'value':-1},
            {'name':'distance_front_right', 'value':-1},
            {'name':'distance_right', 'value':-1},
            {'name':'air_quality', 'value':-1},
            {'name':'temperature', 'value':-1},
           
]

modes = [
        {'name':'BOOTING','fn_name':'fn_boot'},
        {'name':'IDLE','fn_name':'fn_idle'},
        {'name':'PATROL','fn_name':'fn_patrol'},
        {'name':'ALERT','fn_name':'fn_alert'},
        
]

def main():
    start_robot()
    while(1):
        check_events()
        scan_environment()
        time.sleep(1)


def start_robot():
    print("Starting robot...")

def check_events():
    print("Polling for events")

def scan_environment():
    print("Scanning environment")
    for sensor in sensors:
        res = get_sensor_measurement(sensor['name'])
        print(sensor['name'] + ' = ' + str(res))

def get_sensor_measurement(sensor_name):
    return random.randint(1,9)



def fn_boot():
    print('booting...')

main()

        