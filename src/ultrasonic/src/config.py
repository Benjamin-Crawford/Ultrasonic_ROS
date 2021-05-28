#!/usr/bin/env python
#The purpose of this file is to create a lot of variables that will contain settings that will be later utilized in the package...
URM13_ADDRESSES = [0x10,0x11,0x12,0x13]
RANGING_MODE = 0 #0 for long ranging mode, 1 for short ranging mode
DETECT_MODE = 1 #0 for auto detection, 1 for trigger detection
NUM_GROUPS = 1 #defines the number of firing groups to alleviate crosstalk issues
WAIT_TIME = 0.07 #time to wait between trigger and read

#indexes of the sensors in each group leave empty if not using that group
GROUP_MEMBERS = [[0,1,2,3]] 
