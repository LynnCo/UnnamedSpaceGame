#galaxymap.py
#import as gmap

#creates a 2d galaxy map with many qualities

#call galaxymap.get.[quality] for all your needs

import random
import lynn_custom as LC
import math

#[classes]
#galaxy_gen: map size, initializes other classes
#element_gen: very carefully tuned element distributions
#star_gen: creates stars
#system_gen: defines system qualities
#events_gen: defines system events
#constellation_gen: defines constellation qualities
#developement: late term qualities
#get: a collection of any variable external functions would need

#TODO
#star names
#developement
#get

#galaxy control
class galaxy_gen (object):
    
    #map x
    h = 50
    #map y
    v = 150
    #list tuple
    map = list()
    for x in range(h):
        for y in range(v):
            map.append((x,y))
    #galaxy_gen.map
    
    def __init__ (self):
        ele = element_gen()
        star = star_gen()
        sys = system_gen()
        event = events_gen()
        const = constellation_gen()
        #getter = get()
        galaxy_gen.test()
    
    def test ():   
        for i in range(1):
            x,y = star_gen.map.pop()
            print()
            print("\texample star")
            print("{:>15}".format("({}x,".format(x)),"{}y)".format(y))
            print("{:>15}".format("mass:"),"{:,.0f}Mg".format(100*round(system_gen.real_mass[x,y],1)))
            print("{:>15}".format("luminosity:"),"{:.0f}%".format(system_gen.luminosity[x,y]))
            print("{:>15}".format("planets:"),"{}".format(system_gen.planets[x,y]))
            print("{:>15}".format("asteroids:"),"{:.0f}%".format(system_gen.asteroids[x,y]))
            print("{:>15}".format("gas:"),"{:.0f}%".format(system_gen.gas[x,y]))
            print("{:>15}".format("mine yield:"),"lvl {}".format(system_gen.mine_yield[x,y]))
            print("{:>15}".format("radiation:"),"lvl {}".format(system_gen.radiation[x,y]))
            print("{:>15}".format("gravity dsrpt:"),"lvl {}".format(system_gen.gravity_disrupt[x,y]))
            print("{:>15}".format("events:"),"{}".format(events_gen.events[x,y]))
            print("{:>15}".format("constellation:"),"{}".format(constellation_gen.in_const[x,y]))
        
    null = 0
 
#element distribution control
class element_gen (object):
    
    #[x,y] = value
    lights = dict()
    normals = dict()
    heavies = dict()
    exotics = dict()
    
    #generates lights
    #distribution: 50 +- 25
    for (x,y) in galaxy_gen.map: 
        lights[x,y] = random.randint(10,90)
    for (x,y) in lights.keys():
        if lights[x,y]<0: lights[x,y]=0
    l_ave = LC.average(lights.values())
    l_dev = LC.st_dev(lights.values())
    
    #generates normals
    #distribution: 30 +- 10
    for (x,y) in galaxy_gen.map:
        if lights[x,y]>l_ave-l_dev*1:
            normals[x,y] = random.gauss(85,22)
    normals = LC.aggregrate(2,normals,3,3)
    for (x,y) in normals.keys():
        if normals[x,y]<0: normals[x,y]=0
    n_ave = LC.average(normals.values())
    n_dev = LC.st_dev(normals.values())
        
    #generates heavies
    #distrition: 20 +- 5
    for (x,y) in normals.keys():
        if normals[x,y]>n_ave-n_dev*0.75:
            heavies[x,y] = (2*normals[x,y] + lights[x,y])*0.38
    #clustering
    heavies = LC.aggregrate(3,heavies,6,6)
    for (x,y) in heavies.keys():
        if heavies[x,y]<0: heavies[x,y]=0
    h_ave = LC.average(heavies.values())
    h_dev = LC.st_dev(heavies.values())
    
    #generates exotics
    #distribution: 2.5 +- 1.5
    for (x,y) in heavies.keys():
        if heavies[x,y]>h_ave-h_dev*0.5:
            exotics[x,y] = random.gauss(5,1)
    #drop off significantly at the edge
    exotics = LC.aggregrate(4,exotics,10,10)
    for (x,y) in exotics.keys():
        if exotics[x,y]<0: exotics[x,y]=0
    e_ave = LC.average(exotics.values())
    e_dev = LC.st_dev(exotics.values())
    
    #testing   
    
    # LC.write_to_chart(lights,50,150,"lights.csv")
    # LC.write_to_chart(normals,50,150,"normals.csv")
    # LC.write_to_chart(heavies,50,150,"heavies.csv")
    # LC.write_to_chart(exotics,50,150,"exotics.csv")
    
    # print("lights")
    # print(round(l_ave,0))
    # print(round(l_dev,0))
    # print(len(lights))
    # print()
    # print("normals")
    # print(round(n_ave,0))
    # print(round(n_dev,0))
    # print(len(normals))
    # print()
    # print("heavies")
    # print(round(h_ave,0))
    # print(round(h_dev,1))
    # print(len(heavies))
    # print()
    # print("exotics")
    # print(round(e_ave,1))
    # print(round(e_dev,1))
    # print(len(exotics))
    # print()
    
    null = 0

#places stars
class star_gen (object):

    #convientently scaled element dictionaries
    #all scaled to the lights average
    l_s = dict()
    n_s = dict()
    h_s = dict()
    e_s = dict()
    #list of all stars
    map = list()
    #star attributes
    #[x,y] = value
    mass = dict()
    
    for (x,y) in galaxy_gen.map:
        #scale your elements
        try: l_s[x,y] = element_gen.lights[x,y]
        except KeyError: l_s[x,y] = 1
        
        try: n_s[x,y] = element_gen.normals[x,y]*element_gen.l_ave/element_gen.n_ave
        except KeyError: n_s[x,y] = 1
        
        try:h_s[x,y] = element_gen.heavies[x,y]*element_gen.l_ave/element_gen.h_ave
        except KeyError: h_s[x,y] = 1
        
        try: e_s[x,y] = element_gen.exotics[x,y]*element_gen.l_ave/element_gen.e_ave
        except KeyError: e_s[x,y] = 1
        #get (stellar) mass
        mass[x,y] = l_s[x,y]+n_s[x,y]+h_s[x,y]
      
    #if you have above (ratio) mass in that location
    bot = LC.percentile(LC.values_to_list(mass),0.88)
    #flag area for star placement
    flag = dict()
    for (x,y) in galaxy_gen.map:
        if (bot<mass[x,y]): flag[x,y] = mass[x,y]
    
    #star creation
    stars = 0
    map = list()
    #for every location flagged for star creation
    for (x,y) in flag.keys():
        #if stars
        if stars>0:
            #and if they are all not too close
            for (a,b) in map:
                #closeness takes into account both s(ize) and d(istance) fac(tors) 
                d_fac = LC.linear_rescale(1,15,2,0,LC.dist_2d(x,y,a,b))
                s_fac = LC.linear_rescale(320,530,0,1,mass[x,y]+mass[a,b])
                if (d_fac*s_fac<0.63):
                    not_too_close = 1
                else:
                    not_too_close = 0
                    break
            if not_too_close:
                map.append((x,y))
                stars += 1
        #if there aren't any stars then make one here
        else:
            map.append((x,y))
            stars += 1        
    #flag isn't needed anymore so we don't want it lying around
    flag.clear()
    print("{} Total Stars".format(stars))
    #LC.write_to_chart(map,50,150,"star_map.csv")
 
#fills out the star systems
class system_gen (object):

    mass = dict()
    real_mass = dict()
    luminosity = dict()
    planets = dict()
    asteroids = dict()
    gas = dict()
    mine_yield = dict()
    radiation = dict()
    gravity_disrupt = dict()
    
    #mass
    #used for calculations
    #210 +- 10
    for (x,y) in star_gen.map:
        mass[x,y] = star_gen.mass[x,y]
        
    #real_mass
    #used for display
    #50 +- 25
    for (x,y) in star_gen.map:  
        real_mass[x,y] = LC.linear_rescale(180,230,0,100,mass[x,y])
    
    #luminosity
    #50 +- 25
    for (x,y) in star_gen.map:
        score = star_gen.e_s[x,y] + mass[x,y]
        score = LC.linear_rescale(215,295,0,100,score)
        if (score < 0): score = 0
        if (score > 100): score = 100
        luminosity[x,y] = score

    #planets
    #5 +- 2.5
    for (x,y) in star_gen.map:
        v1 = star_gen.n_s[x,y]
        v2 = star_gen.h_s[x,y]
        v3 = mass[x,y]
        score = v1+v2+0.25*v3
        score = math.floor(LC.linear_rescale(148,212,0,10,score))
        if (score < 0): score = 0
        planets[x,y] = score
    
    #asteroids
    #50 +- 25
    for (x,y) in star_gen.map:
        v1 = star_gen.n_s[x,y]
        v2 = star_gen.h_s[x,y]
        score = 0.5*v1+1.5*v2
        score = LC.linear_rescale(110,155,0,100,score)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        asteroids[x,y] = score
    
    #gas
    #50 +- 25
    for (x,y) in star_gen.map:
        v1 = star_gen.l_s[x,y]
        v2 = mass[x,y]
        score = v1+0.1*v2
        score = LC.linear_rescale(75,125,0,100,score)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        gas[x,y] = score
        
    #mine_yield
    #5 +- 2.5
    for (x,y) in star_gen.map:
        score = math.floor(LC.linear_rescale(50,80,0,10,star_gen.h_s[x,y]))
        if (score > 10): score = 10
        elif (score < 1): score = 1    
        mine_yield[x,y] = score
    
    #radiation
    #5 +- 2.5
    for (x,y) in star_gen.map:
        v1 = star_gen.e_s[x,y]
        v2 = luminosity[x,y]
        score = v1+v2
        score = math.floor(LC.linear_rescale(10,180,0,10,score))
        if (score > 10): score = 10
        elif (score < 1): score = 1
        radiation[x,y] = score
        
    #gravity_disrupt
    #5 +- 2.5
    for (x,y) in star_gen.map:
        v1 = mass[x,y]
        v2 = planets[x,y]
        v3 = asteroids[x,y]
        score = v1+10*v2+0.3*v3
        score = math.floor(LC.linear_rescale(200,330,0,10,score))
        if (score > 10): score = 10
        elif (score < 1): score = 1
        gravity_disrupt[x,y] = score

#assigns events to systems
class events_gen (object):

    #used for making some stats
    boon = ["supply base","special substance"]
    hazard = ["pirate raid","collision","crew anamoly","malfunction"]
    events = dict()

    def __init__ (self): 
    
        self.events = events_gen.events
    
        #event definitions
        #to add a new event, add it here and give it a function
        e_def = dict()
        e_def["supply base"] = self.supply_base
        e_def["special substance"] = self.special_substance
        e_def["distress beacon"] = self.distress_beacon
        e_def["pirate raid"] = self.pirate_raid
        e_def["collision"] = self.collision
        e_def["crew anamoly"] = self.crew_anamoly
        e_def["malfunction"] = self.malfunction
        
        #tally up events
        tally = dict()
        for key in e_def.keys():
            tally[key] = 0
        
        for (x,y) in star_gen.map:
            #event v(alue) dictionary
            v = dict()
            for (key,val) in e_def.items():
                v[key] = val(x,y)
            #list of all events sorted by value 
            e_list_sorted = LC.y_dict_sort(v)
            #get the top ones
            top = list()
            for i in range(3):
                temp = e_list_sorted.pop()
                top.append(temp)
                tally[temp] += 1
            self.events[x,y] = top
            
        print()
        print("{:20}".format("[event]"),"[chance]")
        t_list = LC.y_dict_sort(tally)
        for key in t_list:
            print("{:20}".format("{}".format(key)),"{:.2g}".format(round(tally[key]/star_gen.stars,2)))
    
    #boon
    def supply_base (self,x,y):
        v1 = system_gen.planets[x,y]
        v2 = system_gen.mine_yield[x,y]
        score = LC.linear_rescale(5,15,0,80,v1+v2)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score
    
    #boon
    def special_substance (self,x,y):
        score = LC.linear_rescale(0,50,0,35,star_gen.e_s[x,y])
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score

    #nuetral
    def distress_beacon (self,x,y):
        v1 = system_gen.planets[x,y]
        v2 = system_gen.asteroids[x,y]
        score = LC.linear_rescale(0,100,0,40,10*v1+v2)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score

    #hazard    
    def pirate_raid (self,x,y):
        v1 = self.supply_base(x,y)
        v2 = system_gen.asteroids[x,y]
        score = LC.linear_rescale(0,150,0,60,v1+v2)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score

    #hazard
    def collision (self,x,y):
        v1 = system_gen.luminosity[x,y]
        v2 = system_gen.asteroids[x,y]
        score = LC.linear_rescale(0,100,0,50,v1+v2) 
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score

    #hazard
    def crew_anamoly (self,x,y):
        v1 = system_gen.radiation[x,y]
        v2 = star_gen.e_s[x,y]
        score = LC.linear_rescale(0,100,0,50,5*v1+v2)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score

    #hazard
    def malfunction (self,x,y):
        v1 = self.collision(x,y)
        v2 = self.crew_anamoly(x,y)
        score = LC.linear_rescale(0,100,0,50,v1+v2)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score
       
#constellation grouping
class constellation_gen (object):

    #[name] = num
    num = dict()
    #[name] = ([x,y], [x,y], ...)
    core_name = dict()
    #[name] = suffix
    suffix = dict()
    #[num+core_name+suffix] = [(x,y),(x,y),...]
    full_name = dict()
    #([x,y]) = full_name[x,y]
    in_const = dict()
    #[name] = value
    center = dict()
    size = dict()

    def __init__ (self):
        
        cg = constellation_gen

        #gets your core name
        tagcodes = LC.clusters(star_gen.map,6,10)
        name_list = ["Corvus","Crux","Gemini","Sagittarius","Antila","Aries","Aquarius","Argo Navis","Orion","Perseus","Andromeda","Coma Berenices","Sanctum","Sol","Centauri","Targus","Lynx","Erite","Volaran","Prospero Magus","Aluna Borealis"]
        cg.core_name = tagcodes.namer(name_list)
        
        #assigns centers
        for (this_const,star_list) in cg.core_name.items():
            cg.center[this_const] = LC.find_center(star_list)
        #assigns sizes
        for (this_const,star_list) in cg.core_name.items():
            cg.size[this_const] = len(star_list)
  
        #since we might change a core name we have to work on a copy
        core_name_copy = cg.core_name.copy()
        #used list
        used = list()
        #list of suffixes that all run the same way
        suffix_list = ["Prime","Cluster","Cloud","Minor","Major","Concorda","Extremus"]
        function_key = {"Prime":cg.first,"Cluster":cg.dense,"Cloud":cg.sparse,"Minor":cg.few,"Major":cg.many,"Concorda":cg.peace,"Extremus":cg.danger}
        
        #for every unique constellation, without a suffix
        for (this_const,star_list) in core_name_copy.items():
            if cg.should_number(this_const):
                cg.num[this_const] = str(cg.size[this_const])
            try:
                cg.suffix[this_const]
                continue
            except KeyError:
                if ("AB" not in used):
                    #run the function
                    (flag,other_const) = cg.a_b(this_const)
                    #see if it was true
                    if flag:
                        #if so, delete the curret name
                        del cg.core_name[this_const]
                        beta = other_const+" Beta"
                        #put it back in with its new suffix and core name, added as a core name
                        cg.core_name[beta] = star_list
                        #give the other value its new suffix, assign empty suffix for this one
                        cg.suffix[other_const] = "Alpha"
                        cg.suffix[beta] = ""
                        
                        #then pop and re-enter center point with new key
                        tempc = cg.center.pop(this_const)
                        cg.center[beta] = tempc
                        #same with size
                        temps = cg.size.pop(this_const)
                        cg.size[beta] = temps
                        
                        used.append("AB")
                        continue
                #run through all the similar ones
                for this_suffix in suffix_list:
                    if (this_suffix not in used):
                        flag = function_key[this_suffix](this_const)
                        if flag:
                            cg.suffix[this_const] = this_suffix
                            used.append(this_suffix)
                            continue
                            
        #define full names
        for (name,s_list) in cg.core_name.items():
            this_name = str()
            this_name += name
            try: this_name += " "+cg.suffix[name]
            except KeyError: pass
            try: this_name += " "+cg.num[name]
            except KeyError: pass
            cg.full_name[this_name] = s_list
        
        # counter = 0
        # new = cg.full_name.copy()
        # for (name,s_list) in new.items():
            # del cg.full_name[name]
            # cg.full_name[counter] = s_list
            # counter += 1
        
        for (key,value) in cg.full_name.items():
            for star in value:
                cg.in_const[star] = key
        
        # LC.write_to_chart(cg.in_const,50,150,"constellations.csv")
        
        print("\n[Constellations]")
        for print_names in cg.full_name.keys():
            print(print_names)

    #constellation renaming parameters  

    #pre
    #ex: 3-Centauri
    #less than a certain number of stars
    def should_number (this):
        size_list = list()
        for siz in constellation_gen.size.values():
            size_list.append(siz)
        if constellation_gen.size[this]<LC.percentile(size_list,0.5):
            assign = 1
        else:
            assign = 0
        return assign    
    
    #suf, core
    #[LargerConst] Alpha, [LargerConst] Beta
    #two nearby systems, one a bit larger than the other
    #runs for smaller star
    def a_b (this):
        range_to = dict()
        #build range to constellation
        for other in constellation_gen.core_name.keys():
            #nondescriptive variable names 
            o = constellation_gen.center[other]
            t = constellation_gen.center[this]
            if not other==this:
                range_to[other] = LC.dist_2d(o[0],o[1],t[0],t[1])
        #get the closest "constellation"
        range_list = LC.y_dict_sort(range_to)
        closest = range_list[0]
        #check size
        if (1.2*constellation_gen.size[this]<constellation_gen.size[closest]):
            assign = 1
            larger_const = closest
        else:
            assign = 0
            larger_const = "null"   
        return (assign,larger_const)
        
    #suf
    #Prime
    #closest to 0,0
    def first (this):
        range_to = dict()
        for (this_const,loc) in constellation_gen.center.items():
            range_to[this_const] = (loc[0]**2+loc[1]**2)**0.5
        range_list = LC.y_dict_sort(range_to)
        if (this==range_list[0]):
            assign = 1
        else:
            assign = 0
        return assign
    
    #suf
    #Cluster
    #most dense
    def dense (this):
        range_to = dict()
        for (const_i,c) in constellation_gen.center.items():
            sum_diff = 0
            for loc in constellation_gen.core_name[const_i]:
                sum_diff += LC.dist_2d(c[0],c[1],loc[0],loc[1])
            range_to[const_i] = sum_diff/constellation_gen.size[const_i]
        range_list = LC.y_dict_sort(range_to)
        if (this==range_list[0]):
            assign = 1
        else:
            assign = 0
        return assign
        
    #suf
    #Cloud
    #least dense
    def sparse (this):
        range_to = dict()
        for (const_i,c) in constellation_gen.center.items():
            sum_diff = 0
            for loc in constellation_gen.core_name[const_i]:
                sum_diff += LC.dist_2d(c[0],c[1],loc[0],loc[1])
            range_to[const_i] = sum_diff/constellation_gen.size[const_i]
        range_list = LC.y_dict_sort(range_to)
        #the only difference from dense()
        if (this==range_list.pop()):
            assign = 1
        else:
            assign = 0
        return assign
        
    #suf
    #Concorda
    #most peaceful
    def peace (this):
        boon_score = dict()
        for (const_i,stars) in constellation_gen.core_name.items():
            num_boons = 0
            for x,y in stars:
                for boon_i in events_gen.events[x,y]:
                    if boon_i in events_gen.boon:
                        num_boons += 1
            boon_score[const_i] = num_boons
        ordered_list = LC.y_dict_sort(boon_score)
        if (this==ordered_list.pop()):
            assign = 1
        else:
            assign = 0
        return assign
        
    #suf
    #Extremus
    #most dangerous
    def danger (this):
        hazard_score = dict()
        for (const_i,stars) in constellation_gen.core_name.items():
            num_hazards = 0
            for x,y in stars:
                for hazard_i in events_gen.events[x,y]:
                    if hazard_i in events_gen.hazard:
                        num_hazards += 1
            hazard_score[const_i] = num_hazards
        ordered_list = LC.y_dict_sort(hazard_score)
        if (this==ordered_list.pop()):
            assign = 1
        else:
            assign = 0
        return assign
        return assign
        
    #suf
    #Minor
    #least stars
    def few (this):
        if (this==LC.y_dict_sort(constellation_gen.size)[0]):
            assign = 1
        else:
            assign = 0
        return assign

    #suf
    #Major
    #most stars
    def many (this):
        if (this==LC.y_dict_sort(constellation_gen.size).pop()):
            assign = 1
        else:
            assign = 0
        return assign
        
    null = 0
    
#star types and names!
        
#all the things you'd ever need
class get (object):
    
    pass
    
gal = galaxy_gen()