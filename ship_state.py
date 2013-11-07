#ship_state.py
#import as ship

class hull (object):
    '''general hull strength'''

    #0 to 100. <0 and you're dead
    integrity = 100
    
    #change integrity for different types of damage
    #internal, collission, weapons fire, etc...

class location (object):
    '''your place in space'''

    x = 0
    y = 0
    jump_history = list()
        
    def get ():
        return (x,y)
        
    def set (xn,yn):
        x = xn
        y = yn
        location.jump_history.append((xn,yn))
        
#your stuff
class equipment (object):
    '''what your ship is made of'''

    #core
    class generators (object):
        crew = dict()
        crew["type"] = "eng"
        crew["min"] = 0
        crew["max"] = 1
        #structural integrity
        integrity = 100
        power = 0
        #complex systems might just fail randomly
        complexity = 1
    class life_support (object):
        '''
        food, medical, air
        '''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        integrity = 100
        effectiveness = 0
        complexity = 1
        power_draw = 0
    class quarters (object):
        effectiveness = 0
        power_draw = 0
    class bridge (object):
        '''
        the bridge controls many of the more complex
        space craft system. bridge effectiveness influences
        navigation, scanning, and weapons systems.
        '''
        crew = dict()
        crew["type"] = "cmd"
        crew["min"] = 0
        crew["max"] = 1
        effectiveness = 0
        complexity = 1
        power_draw = 0
    class FTL (object):
        '''faster than light drive. uses AntiMatter to operate'''
        crew = dict()
        crew["type"] = "eng"
        crew["min"] = 0
        crew["max"] = 1
        integrity = 100
        #AU/day
        speed = 1
        #mass/AU
        fuel_factor = 1
        complexity = 1
        power_draw = 0
    class sublight (object):
        '''sublight drive. burns gases to operate'''
        crew = dict()
        crew["type"] = "eng"
        crew["min"] = 0
        crew["max"] = 1
        integrity = 100
        speed = 1
        efficiency = 1
        complexity = 1
        power_draw = 0
        
    #acquisiton
    class AM_array (object):
        '''refill your FTL drive'''
        effectiveness = 0
        power_draw = 0
    class solar_array (object):
        '''charge up on the sun'''
        effectiveness = 0
    class miner_shuttle (object):
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        count = 0
        effectiveness = 0
    class gas_probe (object):
        count = 0
        effectiveness = 0
    
    #QOL
    class ship_weapons (object):
        '''defense against large things'''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        intregity = 100
        effectiveness = 0
    class PD_weapons (object):
        '''defense against small things'''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        effectiveness = 0
    class LR_scanner (object):
        '''scan distance systems'''
        crew = dict()
        crew["type"] = "eng"
        crew["min"] = 0
        crew["max"] = 1
        effectiveness = 0
    class probe_scanner (object):
        '''for scanning large nearby bodies'''
        count = 0
        effectiveness = 0
    class armor (object):
        '''physical armor'''
        integrity = 0
        effectiveness = 0
    class shielding (object):
        '''radiation shielding'''
        coverage = 0
        effectiveness = 0
    class cargo (object):
        '''the cargo bay is used for docking, repairs, and storage'''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        size = 0
        repair_rate = 0
        integrity = 100
        
        p_f = dict()
        

class supplies (object):
    '''things you put in a cargo bay'''
    
    biomass = 0
    materials = 0
    AM = 0
    goods = 0

class crew (object):
    '''your trusted companions'''
    
    #[crew_name] = (position,morale)
    #position = "cmd" or "eng" or "gen"
    #command, engineering, general
    member = dict()