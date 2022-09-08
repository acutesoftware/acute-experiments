# ima_robot.py
# definition file for robot 
# simple robot
# 

robot_name="Robby"
robot_id="ROBOT_01"
network_id ="54AE231B0802A1D409"
security_level="LOW"  # for testing
auto_generated='N'
definition_file_version = 0.1
author="Duncan"
date_updated='2022-09-08 18:48'
inputs = ['camera', 'light','sound', 'network']
outputs = ['voice', 'log', 'network']

poll_frequency=1

def generate_output(txt):
    print(robot_name  + '[' + robot_id + ']:  (TODO - voice) ' + txt)

def read_input():
    for input in inputs:
        #print(input
        pass

    return which_sensor_changed()

def process_command(cmd):
    """
    this runs a command 
    """    
    print('processing ' + cmd)

def which_sensor_changed():
    """
    return the latest sensor change
    (no need to process every sensor every 100mS)
    """
    import random
    return random.choice(inputs)