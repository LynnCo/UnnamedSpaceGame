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
import galaxy as gal

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
#travel events
#all scale with jump time
#check jump accuracy also???
#
#either dropout or
#one of the miscal events
#those being:
#miscalulation, alt_pull, slingshot
#NO WAIT
#getting a drop out just pulls from a 
#miscal event
#...yea
#
#WAIT EVEN BETTER!!!!
#the events are a progression of badness
#each checking off the last
# miscal -> alt -> sling
#
#in addition to a radiation event
#rad_dose (electronics) and/or
#rad_sickness (crew)
def dropout ():
    #functional effectiveness of FTL drive
    pass
def miscalculation ():
    #jump dist
    pass
def alt_pull ():
    #nearby star, high relative mass
    pass
def slingshot ():
    #high jump velocity
    pass
#formerly rad_dose
def overload ():
    #works off sheilding
    pass
#formly rad_sickness
def subspace_sickness ():
    #sheilding, crew count
    pass