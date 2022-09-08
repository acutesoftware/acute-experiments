# ima_console.py
# definition file for robot 
# console application
# 

robot_name="Bob"
robot_id="CONSOLE_01"
network_id ="54AE231B0802A1D409"
security_level="LOW"  # for testing
auto_generated='N'
definition_file_version = 0.1
author="Duncan"
date_updated='2022-09-08 18:41'
inputs = ['keyboard', 'network']
outputs = ['screen', 'log', 'network']

poll_frequency=0.01

def generate_output(txt):
    print(robot_name + '[' + robot_id + ']: ' + txt)

def read_input():
    """
    Normally inputs are polled from main brain but console
    sits and waits for user to enter commands (no events)
    """
    ip = input('>')
    return ip
    
def process_command(cmd):
    """
    this runs a command 
    """    
    print('executing ' + cmd)