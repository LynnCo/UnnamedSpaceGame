#travel_events.py
#import as TE

#instanced on movement between systems

#accessed:
#FTL drive params, sheilding params, system gravity disrupt
#inputs:
#jump_to(x,y), jump_from(x,y)
#output:
#an event, if one occurs

import ship_state as ship
import galaxy_map as gmap

class pulse (object):
    '''
    asks whether or not an event is going to occur on this instance of movement
    input: where you are, where you are going
    '''
    
    def __init__ (self,x1,y1,x2,y2)
    
        #e_list is the value we are going to call to see if anything happened
        e_list = list()
       
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        move_event = self.move()
        rad_event = self.rad()
        if move_event:
            e_list.append(move_event)
        if rad_event:
            e_list.append(rad_event)
    
    #pulse movement events
    def move (self):
        #initialize dropout check
        #if dropout check > some value, return dropout (str)
        #otherwise, initiate miscal events
        #if miscal check (any of them) > some value, return the higest one's string
        return 0
        
    #pulse radiation events
    def rad (self):
        return 0
    
class do (object):
    '''
    pulls how influential the particular events are going to be
    input: the event
    '''
    
    def __init__ (self,event):
        pass 