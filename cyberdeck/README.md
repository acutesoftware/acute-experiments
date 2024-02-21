## Cyberdeck - secure standalone PC



The intent is to design a secure, portable stand alone computer to be used for ITNOBAN. This will show the user exactly what is going on and to assist with environmental awareness.

The initial design is a cyberdeck because they look cool, and it will need a lot of hardware testing, config and tweaking to work out what is useful.

The final 'end user' design will be a lot simpler (interface wise), infact it probably wont have (or shouldn't have) a lot of knobs and dials to configure things - it will likely be a voice activated / menu driven / event driven thing that quietly assists the user.

But, for now - we are going to make it will lots of bells and whistles!

![Front Panel](https://github.com/acutesoftware/acute-experiments/blob/master/cyberdeck/cyberdeck_03.png)

Image of front panel

### Next Steps

1. get requirements listed
2. work out design elements
3. shopping list and parts needed
4. build steps
5. testing
6. real world use


### Requirements
Export the p_menu table to get the list of menu commands which relate directly to functions to be done.

Each requirement is grouped into the following main areas
 - Audio
 - Data
 - Misc
 - Network
 - Radio
 - Robot
 - Video

 Requirements may span multiple areas but generally have one main area they can live in.

 Each area has a root folder and one main python module for that area (which can call as many additional programs as needed).

 Each requirement is a single python script 
 `\[area]\fn_[area]_[requirementName].py`


### Features
The following features are built into the cyberdeck

Export the o_features table which has a list of the components to use.

Another table will map how these are built - ie which parts are used to make a features
(eg Audio Amp needs: vol control, audio amplifier, speaker, on/off switch, 3.5mm input, 3.5mm ouput)

### Requirements mapped to features

Once the features are thought out - map them to requirements to ensure that all requirements can be met by the design.

