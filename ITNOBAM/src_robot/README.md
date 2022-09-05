## Robot Source
Source code for moveable unit for ITNOBAM

Note that any source code here is for testing of the concepts and is NOT useful for any real world applications - this is more of a testbed at this stage to see what is possible with this idea.

#### Running Modes

Initially the system runs in DEV mode which will make it possible to actually do the development - needs to be some sort of indicator in case DEV mode is activated after moved to production use (probably should not ever happen [?])

Normal operation (PROD) means that the system has locked source data sets and treats all networks as potentially hostile.

The method to detect people could include
- encrypted imagesets to allow facial recognition
- encrypted voice patterns
- aggregates of movement styles to recognise people (gait, height, sounds of footsteps)

Any image detection process needs to use camera in conjuntion with other sensors especially distance measurement to stop holding up photos of people to bypass security.

#### Hardware Abilities

The abilities of the robot need to be specified in the robot_config.py
by uncommenting hardware the robot has.

this is used to work out what code and tasks are possible

Movement

````

    [ ] move forward / backwards
    [ ] turn on circle ( Left / Right rotating )
    [ ] strafe left / right


````

Arm

````
    
    [ ] has arm
    [ ] move X axis ( left /right)
    [ ] move Y axis ( forward / back)
    [ ] move Z axis ( up / down)
    [ ] rotate X axis ( left /right)
    [ ] rotate Y axis ( forward / back)
    [ ] rotate Z axis ( up / down)
    [ ] gripper

````

### Software Abilities

This is the list of standard tasks that the system can do, which takes into account the hardware and sensors available.

#### Communication and Human detection

Tasks that the system can assist with in regards to verifying humans (carers, family, visitors) to give context for the user.

````

    [X] Show list of people in room
    [X] Notify user of problem
    [ ] Verify people in room
    [ ] User asks for humand to verify situation
    [ ] Contact trusted human

````

#### Environmental detection

Checking the environment for potential problems

````

    [ ] is the stove on (temp sensor near stove, visible check of knobs, optional link to oven A/C drain)
    [ ] are the doors locked
    [X] is the house on fire (direct link from smoke detectors)

````

#### Movement

Tasks the moveable robot can do

````

    [X] Follow user (follow means be nearby but stay OUT of the way in case of tripping)
    [ ] return to recharge (when user is asleep / out with carers, move to docking station for recharge)
    [ ] Patrol house (do a circuit of house to check for issues)
    [ ] Sweep floors (optional vaccum / mop when user is away)

````


