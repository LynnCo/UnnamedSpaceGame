#action.py
#import as action

#things to do once you enter a system
#defined from system features and ship capabilities
#a single class that is instanced on entry into the system
#(from travel_rest)

import galaxy as gal
import ship_state as ship

class pull_available (object):
    def __init__ (self):
        pass
    

class do (object):
    '''
    pulls how influential the particular events are going to be
    input: the event
    '''

#actions
class action (object):
    pass
#action collect
class collect (action):
    pass
#action collect gas
class gas (collect):
    #ice giant: low
    #gas giant: med
    #gas cloud: high
    pass
#action collect rock
class rock (collect):
    #asteroid belt
    pass
#action collect bio
class bio (collect):
    #inner planets
    pass
#action collect special_substance
class special_substance (collect):
    #inner: low
    #planetesimal: med
    #comets: high
    pass
#action collect info
class scan (collect):
    #probe planets
    #local area scan
    pass
#action ship
class ship (action):
    pass
#action ship optimize_solar
class optimize_solar (ship):
    pass
#action ship optimize_AM
class optimize_AM (ship):
    pass
#action ship repair
class repair (ship):
    pass
#action supply_base
class supply_base (action):
    pass