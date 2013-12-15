#galaxy.py
#import as gal

#creates a 2d galaxy with many qualities
#call galaxy.get.[quality] for all your needs

import random
import lynn_custom as LC
import math
import re

#galaxy control
class galaxy_gen (object):
    #map x
    h = 0
    #map y
    v = 0
    #list tuple
    map = list()
    def __init__ (self):
        gg = galaxy_gen
        gg.h = 100
        gg.v = 100
        for x in range(gg.h):
            for y in range(gg.v):
                gg.map.append((x,y))
        ele = element_gen()
        star = star_gen()
        sys = system_gen()
        event = events_gen()
        const = constellation_gen()
        cos = cosmetic()
#element distribution control
class element_gen (object):
    #[x,y] = value
    lights=dict();normals=dict();heavies=dict();exotics=dict()
    l_ave=0;l_dev=0;n_ave=0;n_dev=0;h_ave=0;h_dev=0;e_ave=0;e_dev=0
    def __init__ (self):
        eg = element_gen
        #lights 50 +- 25
        for (x,y) in galaxy_gen.map: 
            eg.lights[x,y] = random.gauss(50,25)
        for (x,y) in eg.lights.keys():
            if eg.lights[x,y]<0: eg.lights[x,y]=0
        eg.l_ave = LC.average(eg.lights.values())
        eg.l_dev = LC.st_dev(eg.lights.values())
        #normals 30 +- 10
        for (x,y) in galaxy_gen.map:
            if eg.lights[x,y]>eg.l_ave-eg.l_dev*0.8:
                eg.normals[x,y] = random.gauss(30,10)
        for (x,y) in eg.normals.keys():
            if eg.normals[x,y]<0: eg.normals[x,y]=0
        eg.n_ave = LC.average(eg.normals.values())
        eg.n_dev = LC.st_dev(eg.normals.values()) 
        #heavies 25 +- 5
        for (x,y) in eg.normals.keys():
            if eg.normals[x,y]>eg.n_ave-eg.n_dev*0.8:
                eg.heavies[x,y] = (2*eg.normals[x,y] + eg.lights[x,y])*0.2
        for (x,y) in eg.heavies.keys():
            if eg.heavies[x,y]<0: eg.heavies[x,y]=0
        eg.h_ave = LC.average(eg.heavies.values())
        eg.h_dev = LC.st_dev(eg.heavies.values())
        #exotics 2.5 +- 1.5
        for (x,y) in eg.heavies.keys():
            if eg.heavies[x,y]>eg.h_ave-eg.h_dev*0.8:
                eg.exotics[x,y] = random.gauss(2.5,1.5)
        for (x,y) in eg.exotics.keys():
            if eg.exotics[x,y]<0: eg.exotics[x,y]=0
        eg.e_ave = LC.average(eg.exotics.values())
        eg.e_dev = LC.st_dev(eg.exotics.values())
        #testing   
        # LC.write_to_chart(lights,50,150,"lights.csv")
        # LC.write_to_chart(normals,50,150,"normals.csv")
        # LC.write_to_chart(heavies,50,150,"heavies.csv")
        # LC.write_to_chart(exotics,50,150,"exotics.csv")
        print("lights");print(round(eg.l_ave,0));print(round(eg.l_dev,0));print(len(eg.lights));print()
        print("normals");print(round(eg.n_ave,0));print(round(eg.n_dev,0));print(len(eg.normals));print()
        print("heavies");print(round(eg.h_ave,0));print(round(eg.h_dev,1));print(len(eg.heavies));print()
        print("exotics");print(round(eg.e_ave,1));print(round(eg.e_dev,1));print(len(eg.exotics));print()
#places stars
class star_gen (object):
    #element dictionaries. all scaled to the lights average
    l_s = dict();n_s = dict();h_s = dict();e_s = dict()
    #list of all stars
    map = list()
    #star attributes. [x,y] = value
    mass = dict()
    def __init__ (self):
        sg = star_gen
        for (x,y) in galaxy_gen.map:
            #scale your elements
            try: sg.l_s[x,y] = element_gen.lights[x,y]
            except KeyError: sg.l_s[x,y] = 1
            try: sg.n_s[x,y] = element_gen.normals[x,y]*element_gen.l_ave/element_gen.n_ave
            except KeyError: sg.n_s[x,y] = 1
            try:sg.h_s[x,y] = element_gen.heavies[x,y]*element_gen.l_ave/element_gen.h_ave
            except KeyError: sg.h_s[x,y] = 1
            try: sg.e_s[x,y] = element_gen.exotics[x,y]*element_gen.l_ave/element_gen.e_ave
            except KeyError: sg.e_s[x,y] = 1
            #get (stellar) sg.mass
            sg.mass[x,y] = sg.l_s[x,y]+sg.n_s[x,y]+sg.h_s[x,y]
        #if you have above (ratio) sg.mass in that location
        bot = LC.percentile(LC.values_to_list(sg.mass),0.9)
        #flag area for star placement
        flag = dict()
        for (x,y) in galaxy_gen.map:
            if (bot<sg.mass[x,y]): flag[x,y] = sg.mass[x,y]
        #star creation
        stars = 0
        #for every location flagged for star creation
        for (x,y) in flag.keys():
            #if stars
            if stars>0:
                #and if they are all not too close
                for (a,b) in sg.map:
                    #closeness takes into account both s(ize) and d(istance) fac(tors) 
                    d_fac = -0.143*math.hypot(x-a,y-b)+2.14
                    s_fac = 0.00476*(sg.mass[x,y]+sg.mass[a,b])-1.52
                    if (d_fac*s_fac<0.63): not_too_close = 1
                    else:not_too_close=0;break
                if not_too_close:sg.map.append((x,y));stars+=1
            #if there aren't any stars then make one here
            else:sg.map.append((x,y));stars+=1        
        #flag isn't needed anymore so we don't want it lying around
        flag.clear()
        print("{} Total Stars".format(stars))
        #print(sg.map)
        #LC.write_to_chart(sg.map,50,150,"star_sg.map.csv")
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
    def __init__ (self):
        syg = system_gen
        #mass. used for calculations. 210 +- 10
        for (x,y) in star_gen.map: syg.mass[x,y] = star_gen.mass[x,y] 
        #real_mass. used for display. 50 +- 25
        for (x,y) in star_gen.map: syg.real_mass[x,y] = 100*round(2*syg.mass[x,y]-360,1)
        #luminosity. 50 +- 25
        for (x,y) in star_gen.map:
            score = star_gen.e_s[x,y] + syg.mass[x,y]
            score = 1.25*score-268.75
            if (score < 0): score = 0
            if (score > 100): score = 100
            syg.luminosity[x,y] = score
        #planets. 5 +- 2.5
        for (x,y) in star_gen.map:
            v1 = star_gen.n_s[x,y];v2 = star_gen.h_s[x,y];v3 = syg.mass[x,y]
            score = v1+v2+0.25*v3
            score = math.floor(0.156*score-23.1)
            if (score < 0): score = 0
            syg.planets[x,y] = score
        #asteroids. 50 +- 25
        for (x,y) in star_gen.map:
            v1 = star_gen.n_s[x,y];v2 = star_gen.h_s[x,y]
            score = 0.5*v1+1.5*v2
            score = 2.22*score-244
            if (score > 100): score = 100
            elif (score < 1): score = 1
            syg.asteroids[x,y] = score
        #gas. 50 +- 25
        for (x,y) in star_gen.map:
            v1 = star_gen.l_s[x,y];v2 = syg.mass[x,y]
            score = v1+0.1*v2
            score = 2*score-150
            if (score > 100): score = 100
            elif (score < 1): score = 1
            syg.gas[x,y] = score
        #mine_yield. 5 +- 2.5
        for (x,y) in star_gen.map:
            score = math.floor(0.333*star_gen.h_s[x,y]-16.7)
            if (score > 10): score = 10
            elif (score < 1): score = 1    
            syg.mine_yield[x,y] = score
        #radiation. 5 +- 2.5
        for (x,y) in star_gen.map:
            v1 = star_gen.e_s[x,y];v2 = syg.luminosity[x,y]
            score = v1+v2
            score = math.floor(0.0588*score-0.588)
            if (score > 10): score = 10
            elif (score < 1): score = 1
            syg.radiation[x,y] = score
        #gravity_disrupt. 5 +- 2.5
        for (x,y) in star_gen.map:
            v1 = syg.mass[x,y];v2 = syg.planets[x,y];v3 = syg.asteroids[x,y]
            score = v1+10*v2+0.3*v3
            score = math.floor(0.0769*score-15.4)
            if (score > 10): score = 10
            elif (score < 1): score = 1
            syg.gravity_disrupt[x,y] = score
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
        # print()
        # print("{:20}".format("[event]"),"[chance]")
        # t_list = LC.y_dict_sort(tally)
        # for key in t_list:
            # print("{:20}".format("{}".format(key)),"{:.2g}".format(round(tally[key]/star_gen.stars,2)))
    #boon
    def supply_base (self,x,y):
        v1 = system_gen.planets[x,y];v2 = system_gen.mine_yield[x,y]
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
        v1 = system_gen.planets[x,y];v2 = system_gen.asteroids[x,y]
        score = LC.linear_rescale(0,100,0,40,10*v1+v2)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score
    #hazard    
    def pirate_raid (self,x,y):
        v1 = self.supply_base(x,y);v2 = system_gen.asteroids[x,y]
        score = LC.linear_rescale(0,150,0,60,v1+v2)
        if (score > 100): score = 100
        elif (score < 1): score = 1
        return score
    #hazard
    def collision (self,x,y):
        v1 = system_gen.luminosity[x,y];v2 = system_gen.asteroids[x,y]
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
        v1 = self.collision(x,y);v2 = self.crew_anamoly(x,y)
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
    in_const_core = dict()
    #[name] = value
    center = dict()
    size = dict()
    def __init__ (self):
        cg = constellation_gen
        #gets your core name
        tagcodes = LC.clusters(star_gen.map,10,20)
        name_list = ["Sideritte","Corvus","Cancer","Lux","Crux","Altoic","Gemini","Gaunt","Sagittarius","Antila","Aries","Aquarius","Argo Navis","Orion","Perseus","Syndra","Karma","Andromeda","Buex","Coma Berenices","Sanctum","Sol","Centauri","Targus","Lynx","Erite","Volaran","Prospero Magus","Aluna Borealis"]
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
            for star in value:cg.in_const[star] = key
        for (key,value) in cg.core_name.items():
            for star in value:cg.in_const_core[star] = key
        # LC.write_to_chart(cg.in_const,50,150,"constellations.csv")
        # print("\n[Constellations]")
        # for print_names in cg.full_name.keys():
            # print(print_names)
    #constellation renaming parameters  
    #less than a certain number of stars
    def should_number (this):
        size_list = list()
        for siz in constellation_gen.size.values():
            size_list.append(siz)
        if constellation_gen.size[this]<LC.percentile(size_list,0.5):assign = 1
        else:assign = 0
        return assign    
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
                range_to[other] = math.hypot(o[0]-t[0],o[1]-t[1])
        #get the closest "constellation"
        range_list = LC.y_dict_sort(range_to)
        closest = range_list[0]
        #check size
        if (1.2*constellation_gen.size[this]<constellation_gen.size[closest]):assign = 1;larger_const = closest
        else:assign = 0;larger_const = "null"   
        return (assign,larger_const)
    #Prime - closest to 0,0
    def first (this):
        range_to = dict()
        for (this_const,loc) in constellation_gen.center.items():
            range_to[this_const] = (loc[0]**2+loc[1]**2)**0.5
        range_list = LC.y_dict_sort(range_to)
        if (this==range_list[0]):assign = 1
        else:assign = 0
        return assign
    #Cluster - most dense
    def dense (this):
        range_to = dict()
        for (const_i,c) in constellation_gen.center.items():
            sum_diff = 0
            for loc in constellation_gen.core_name[const_i]:
                sum_diff += math.hypot(c[0]-loc[0],c[1]-loc[1])
            range_to[const_i] = sum_diff/constellation_gen.size[const_i]
        range_list = LC.y_dict_sort(range_to)
        if (this==range_list[0]):assign = 1
        else:assign = 0
        return assign
    #Cloud - least dense
    def sparse (this):
        range_to = dict()
        for (const_i,c) in constellation_gen.center.items():
            sum_diff = 0
            for loc in constellation_gen.core_name[const_i]:
                sum_diff += math.hypot(c[0]-loc[0],c[1]-loc[1])
            range_to[const_i] = sum_diff/constellation_gen.size[const_i]
        range_list = LC.y_dict_sort(range_to)
        #the only difference from dense()
        if (this==range_list.pop()):assign = 1
        else:assign = 0
        return assign
    #Concorda - most peaceful
    def peace (this):
        boon_score = dict()
        for (const_i,stars) in constellation_gen.core_name.items():
            num_boons = 0
            for x,y in stars:
                for boon_i in events_gen.events[x,y]:
                    if boon_i in events_gen.boon:num_boons += 1
            boon_score[const_i] = num_boons
        ordered_list = LC.y_dict_sort(boon_score)
        if (this==ordered_list.pop()):assign = 1
        else:assign = 0
        return assign
    #Extremus - most dangerous
    def danger (this):
        hazard_score = dict()
        for (const_i,stars) in constellation_gen.core_name.items():
            num_hazards = 0
            for x,y in stars:
                for hazard_i in events_gen.events[x,y]:
                    if hazard_i in events_gen.hazard:num_hazards += 1
            hazard_score[const_i] = num_hazards
        ordered_list = LC.y_dict_sort(hazard_score)
        if (this==ordered_list.pop()):assign = 1
        else:assign = 0
        return assign
        return assign
    #Minor - least stars
    def few (this):
        if (this==LC.y_dict_sort(constellation_gen.size)[0]):assign = 1
        else:assign = 0
        return assign
    #Major - most stars
    def many (this):
        if (this==LC.y_dict_sort(constellation_gen.size).pop()):assign = 1
        else:assign = 0
        return assign
#star types and names! also planet names
class cosmetic (object):
    star_type = dict()
    star_name = dict()
    def __init__ (self):
        self.star_typer()
        self.star_namer()
        #self.planet_namer()
    def star_typer (self):
        cgc = constellation_gen.center
        cgcn = constellation_gen.core_name
        cgs = constellation_gen.size
        cgic = constellation_gen.in_const_core
        #type factor
        t_fac = dict()
        fl = list()
        for (x,y) in star_gen.map:
            const_i = cgic[x,y]
            sum_diff = 0
            for loc in cgcn[const_i]:
                sum_diff += math.hypot(cgc[const_i][0]-loc[0],cgc[const_i][1]-loc[1])
            c = sum_diff/cgs[const_i]*100/8
            e = star_gen.e_s[x,y]*50/40
            m = star_gen.mass[x,y]*10/2
            t_fac[(x,y)] = c+e+m
            fl.append(c+e+m)
        f70 = LC.percentile(fl,0.7)
        f90 = LC.percentile(fl,0.9)
        for (x,y) in star_gen.map:
            if t_fac[x,y]>f90: cosmetic.star_type[(x,y)] = "T"
            elif t_fac[x,y]>f70: cosmetic.star_type[(x,y)] = "B"
            else: cosmetic.star_type[(x,y)] = "S"          
    def star_namer (self):
        for (x,y) in star_gen.map:
            p1 = str();p2 = str();p3 = str()
            p1 = cosmetic.star_type[x,y]
            p2 = LC.to_base((x*y),15)
            p3t = constellation_gen.in_const[x,y]
            p3t = re.split(" +",p3t)
            for word in p3t:
                if type(word)==str: 
                    try: p3 += word[0]
                    except IndexError: pass
                else: p3 += word
            name = p1+p2+p3
            if len(name)==8: name = name[:-2]
            elif len(name)==7: name = name[:-1]
            elif len(name)==5: name += "0"
            elif len(name)==4: name += "00"
            elif len(name)==3: name += "000"
            cosmetic.star_name[x,y] = name
#late term things
class developement (object):
    extras = dict()
    planet_names = dict()
    bio = dict()
    def __init__ (self):
        developement = dv
        #bio
        #planet types
        #extras
        gc = 0
        ac = 0
        cc = 0
        hc = 0
        for coords in star_gen.map:
            dv.extras[coords] = list()
            if dv.gas_cloud(coords):
                dv.extras[coords].append("gas cloud")
                gc += 1
            if dv.asteroid_belt(coords):
                dv.extras[coords].append("asteroid belt")
                ac += 1
            if dv.comets(coords):
                dv.extras[coords].append("comets")
                cc += 1
            if dv.hostile_colony(coords):
                dv.extras[coords].append("hostile colony")
                hc += 1
        print(gc," gas clouds")
        print(ac," asteroid belts")
        print(cc," comets")
        print(hc," hostile colonies")
    def gas_cloud (coords):
        gas = system_gen.gas(coords)>0.7
        pla = system_gen.planets(coords)<5
        if gas and pla:
            return 1
        else:
            return 0
    def asteroid_belt (coords):
        ast = system_gen.asteroids(coords)>0.7
        pla = system_gen.planets(coords)>4
        if ast and pla:
            return 1
        else:
            return 0
    def comets (coords):
        ast = system_gen.asteroids(coords)>0.8
        lum = system_gen.luminosity(coords)>0.8
        pla = system_gen.planets(coords)>5
        if ast and lum and pla:
            return 1
        else:
            return 0
    def hostile_colony (coords):
        return 0
#all the things you'd ever need
#galaxy.get.thing()
class get (object):
    def mass(x,y):return system_gen.real_mass[x,y]
    def luminosity(x,y):return system_gen.luminosity[x,y]
    def planets(x,y):return system_gen.planets[x,y]
    def asteroids(x,y):return system_gen.asteroids[x,y]
    def gas(x,y):return system_gen.gas[x,y]
    def mine_yield(x,y):return system_gen.mineyield[x,y]
    def radiation(x,y):return system_gen.radiation[x,y]
    def gravity_disrupt(x,y):return system_gen.gravity_disrupt[x,y]
    def events(x,y):return events_gen.events[x,y]
    def constellation(x,y):return constellation_gen.in_const[x,y]
    def star_name(x,y):return cosmetic.star_name[x,y]
