# valid_lists.py
# valid lists for robot - central place to define available functions
# 

all_bots = [  # list of bots - keep both data and code in one module for now
    'def_robot',
    'def_console',
    'def_sensor',
    'def_filebot',
    'def_webapp',
]

all_inputs = [  # what can the bot see
    'camera', 
    'light',
    'sound', 
    'network', 
    'keyboard'
    ]

all_outputs = [  # how does the bot commnunicate with the outside world
    'voice', 
    'log', 
    'network', 
    'screen']

all_networks = [  # trivial string to stop casual users starting bot on command line
    '54AE231B0802A1D409',
    '010203040506070809',
]

trusted_humans = [  # which humans should the bot be taking commands from
    'duncan',
    'doctor_mary'
]

all_statuses = [  # what is the bot doing right now
    'BOOTING',
    'IDLE',
    'LEARNING',
    'PLAYING',
    'CHATTING',
    'WORKING',
    'ALERT',
    'DANGER'
]

all_moods = [   # what mood is the bot right now (initially random or based on environment)
    'NORMAL',
    'PLAYFUL',
    'LAZY',
    'NERVOUS'
]

all_goals = [   # what is the goal the bot is working towards
    'ASSIST',
    'GUARD',
    'LEARN',
    'CLEAN',
    'PLAY'
]