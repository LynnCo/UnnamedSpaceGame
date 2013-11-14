#ship_state.py
#import as ship

#a collection of the numbers about the ship
#also used to write in new ship state numbers

class hull (object):
    '''general hull strength'''

    #physical state. 0 -> 100. 0 = destroyed
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
class subsystem (object):
    '''what your ship is made of'''

    #crew = the type and how many people operate this subsystem. (cmd,eng,gen) 0->
    #integrity = physical integrity. is this thing about to break apart. 100 -> 0
    #complexity =  more complex systems may fail more easily. 1 ->
    #effectiveness = how well this component is functioning. 0 -> 1
    #power_out = generators,solar_array
    #always on: life_support,colony_module,bridge
    #FTL: FTL 
    #subspace: AM_array,sublight,PD_weapons,ship_weapons 

    #core
    class generators (object):
        '''provides your power'''
        crew = dict()
        crew["type"] = "eng"
        crew["min"] = 0
        crew["max"] = 1
        integrity = 100
        complexity = 1
        power_out = 0
    class life_support (object):
        '''food, medical, air'''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        integrity = 100
        effectiveness = 0
        complexity = 1
        power_in = 0
    class colony_module (object):
        '''mini habitat, ready to be translated to a new world'''
        integrity = 0
        power_in = 0
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
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
        power_in = 0
    class FTL (object):
        '''faster than light drive. uses AntiMatter to operate'''
        crew = dict()
        crew["type"] = "eng"
        crew["min"] = 0
        crew["max"] = 1
        #ly/day
        speed = 1
        #mass/ly
        fuel_factor = 1
        #optimal distance 9 -> 12ly
        o_dist = 10
        #base inaccuracy 1 -> 2y
        b_iacc = 1.5
        integrity = 100
        effectiveness = 1
        complexity = 1
        power_in = 0

    class sublight (object):
        '''sublight drive. burns gases to operate'''
        crew = dict()
        crew["type"] = "eng"
        crew["min"] = 0
        crew["max"] = 1
        integrity = 100
        
        #AU/day
        speed = 1
        #mass/AU
        fuel_factor = 1
        
        effectiveness = 1
        complexity = 1
        power_in = 0
        
    #acquisiton
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
    class AM_array (object):
        '''refill your FTL drive'''
        effectiveness = 0
        power_in = 0
    class solar_array (object):
        '''charge up on the sun'''
        effectiveness = 0
        power_out = 0
    class miner_shuttle (object):
        '''collects rocks'''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        count = 0
        effectiveness = 0
    class gas_probe (object):
        '''collects gas'''
        count = 0
        effectiveness = 0
    
    #QOL
    class PD_weapons (object):
        '''defense against small things'''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        effectiveness = 0
        power_in = 0
    class ship_weapons (object):
        '''defense against large things'''
        crew = dict()
        crew["type"] = "gen"
        crew["min"] = 0
        crew["max"] = 1
        intregity = 100
        effectiveness = 0
        power_in = 0
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
        #packing factor = how efficiently a thing is stored in your cargo. 0.1 -> 5
        p_f = dict()
        p_f["biomass"] = 1
        p_f["materials"] = 1
        p_f["AM"] = 1
        p_f["goods"] = 1
        

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