#lynn_custom.py
#import as LC

#a collection of all my personal functions

#todo:
#slanted split
#better averaging and cluster functions
#standard deviation
#oscillator
#significant figures rounder

#import
import math
import random
import time
import csv



# I/O



def write_to_chart (collection,h,v,filename):
    '''
    input: dictionary [x,y]=val or list [(x,y),(x,y)...], horizontal, verticle, your_file.csv
    '''
    with open(filename,"w",newline="") as csvfile:
        writer_i = csv.writer(csvfile,dialect="excel")
        if type(collection)==dict:
            for y in range(v):
                row = list()
                for x in range(h):
                    try: row.append(collection[x,y])
                    except KeyError: row.append("")
                writer_i.writerow(row)
                row.clear()
        elif type(collection)==list:
            for y in range(v):
                row = list()
                for x in range(h):    
                    if (x,y) in collection: row.append(1)
                    else: row.append("")
                writer_i.writerow(row)
                row.clear
        else:
            print("Invalid type")

            
            
#DICTIONARIES
            
            
            
def xydictsort (dic):
    '''
    input: dict[x,y]
    output: list[(x,y),(x,y)...] sorted
    '''
    dlist = list()
    for (x,y) in dic:
        dlist.append((x,y))
    dlist.sort()
    return dlist
    
def y_dict_sort (dic):
    '''
    sorts a dictionary by its values
    
    input: dictionary
    output: list(key,key,key...)
    '''
    dlist = list()
    for (k,v) in dic.items():
        dlist.append((v,k))
    dlist.sort()
    out = list()
    for (a,b) in dlist:
        out.append(b)
    return out
            
def values_to_list (dic):
    '''not sure that I even need this'''
    v_list = list()
    for i in dic.values():
        v_list.append(i)
    return v_list
 
 
 
#BASIC MATH
    
    
    
#def sig_figs (val,figs):
    #return rounded_v
    
def st_dev (values):
    '''standard deviation'''
    sum = 0
    av = average(values)
    for x in values:
        sum += ((x-av)**2)
    dev = (sum/(len(values)-1))**0.5
    return dev
    
def average (values):
    return (sum(values)/len(values))

def median (values):
    return (percentile(values,0.5))
    
def percentile (values,ratio):
    '''
    pulls for you the percentile value of a list
    e.x. if ratio = 0.90, gives you the value that is greater than 90% of the list
    '''
    try:
        values.sort()   
        v = list()
        v.append(values[math.floor(len(values)*ratio)])
        v.append(values[math.floor(len(values)*ratio-1)])
        return average(v)
    except IndexError:
        print("ERROR: percentile ratio not valid")

def get_percentile (values,number):
    '''gets the "percentile" of a given number within a list'''
    values.sort
    place = values.index(number)
    return (place/len(values))
   
   

#2D MATH


   
def dist_2d (x1,y1,x2,y2):
    '''distance between two 2d points'''
    dx = x2 - x1
    dy = y2 - y1
    return math.hypot(dx,dy)

def linear_rescale (a1,a2,b1,b2,x):
    '''scales a value according to a linear function'''
    m = (b1-b2)/(a1-a2)
    b = b1 - m*a1
    y = m*x+b
    return y

def find_center (stars):
    point = [0,0]
    x_list = list()
    y_list = list()
    for (x,y) in stars:
        x_list.append(x)
        y_list.append(y)
    point[0] = average(x_list)
    point[1] = average(y_list)
    point = tuple(point)
    return point    
    
def sqr_av (r,map,mod=0.5):
    '''
    square average
    
    for every given point, changes it to the average 
    of all the points that surround it. 
    works on a copy so we don't do a moving average.
    
    inputs: "radius", dict[x,y] = value, mod
    outputs: same dict with new values
    
    [Optional] 
    mod is a ratio the influences value change
    1 = makes the point the average
    0 = disables function
    '''
    t_map = map.copy()
    box = list()
    for h in range(-r,r):
        for v in range(-r,r):
            box.append((h,v)) 
    for (x,y) in map.keys():
        local = list()
        for (h,v) in box:
            try:
                local.append(map[x+h,y+v])
            except KeyError:
                pass
        point_av = average(local)
        diff = (point_av - map[x,y])*mod
        t_map[x,y] = map[x,y] + diff
        local.clear
    return t_map
    
def aggregrate_v2 (map,width,height,mod_c=5):
    '''
    less accurate, but x10 faster
    '''
    box_size = 5
    int1_max = math.ceil(width/box_size)
    int2_max = math.ceil(height/box_size)
    
    map1 = map.copy()

    for int1 in range(1,int1_max+1):
        for int2 in range(1,int2_max+1):
            box = list()
            for x in range(box_size*(int1-1),box_size*int1):
                for y in range(box_size*(int2-1),box_size*int2):
                    try: 
                        box.append(map[x,y])
                    except KeyError:
                        pass
            if box:
                av = average(box)
                for x in range(box_size*(int1-1),box_size*int1):
                    for y in range(box_size*(int2-1),box_size*int2):
                        try:             
                            percentile = get_percentile(box,map[x,y])
                            cluster = linear_rescale(0,1,1/mod_c,1*mod_c/3,percentile)
                            map1[x,y] *= cluster
                        except KeyError: 
                            pass  
    return map1
  
def aggregrate (d,map,mod_c=5,mod_e=5):
    '''
    moves the values into "clumps"
    also decreases values near the edge of the grid
    
    inputs: distance, dict[x,y] = value, clumping, edging
    outputs: same dict with new values
    
    [Optional]
    mod_c influences clumping (min 1)
    mod_e influences edge decrease
    '''
    t_map = map.copy()
    #l(onely) for points near edge
    l = (d+1)**2
    #c(rowded) for points that are not
    c = (2*d+1)**2
    box = list()
    for h in range(-d,d):
        for v in range(-d,d):
            box.append((h,v)) 
    for (x,y) in map.keys():
        local = list()
        for (h,v) in box:               
            try:
                local.append(map[x+h,y+v])
            except KeyError:
                pass                        
        if mod_c:
            percentile = get_percentile(local,map[x,y])
            cluster = linear_rescale(0,1,1/mod_c,1*mod_c/3,percentile)
            t_map[x,y] *= cluster
        if mod_e:    
            edge = linear_rescale(l,c,1/mod_e,1,len(local))
            t_map[x,y] *= edge
        local.clear
    return t_map    
    
   

#GRID TOOLS        
        
        
    
class clusters (object):  
    '''
    clusters is a grid based tool that is used to group 
    2d data sets by splitting them in half constantly
    
    input: a list of (x,y) tuples
    output: [x,y] = "XXXXXX"
    
    "XXXXXX" is the split history. example: ABBBAB
    
    [Optional]
    range refers to the max size of the split groups
    '''      

    def __init__ (self,map,small=5,large=15):
        self.small = small
        self.large = large
        self.splits = 0
        self.tags = dict()
        for (x,y) in map: 
            self.tags[x,y] = str()
        self.limit = len(map)
        self.splitter(map)

    #where you get your output from
    @property
    def get_tags (self): return self.tags
        
    #NEED TO MAKE A DIAGONAL SPLITTER
        
    #where the magic happens
    def splitter (self,points):
        '''
        recursive function that splits up the [x,y] points.
        every other level of split is supposed to be either
        splitting down the middle x or y. the initial run will
        split and tag the points across x, then swap x and y.
        '''
        #this finds the middle point between two central data points
        temp = list()
        for (x,y) in points:
            temp.append(x)
        mid = median(temp)

        #the points go into groups A and B
        points_A = list()
        points_B = list()

        #based on their value relative to the midpoint
        for (x,y) in points:
            if x > mid:
                #and assigns the other way around if needed
                try:
                    self.tags[x,y] = self.tags[x,y]+"A"
                    points_A.append((y,x))
                except KeyError:
                    self.tags[y,x] = self.tags[y,x]+"A"
                    points_A.append((y,x))
            else:
                try:
                    self.tags[x,y] = self.tags[x,y]+"B"
                    points_B.append((y,x))
                except KeyError:
                    self.tags[y,x] = self.tags[y,x]+"B"
                    points_B.append((y,x))
                    
        points_A.sort()
        points_B.sort()
        # print("points   %i" %len(points))
        # print("points A %i" %len(points_A))
        # print("points B %i" %len(points_B))
        # print()
        
        max = random.randint(self.small,self.large)
        #only continue to split if there are >max entries
        #and if you haven't hit the split limit
        if self.splits<self.limit:
            self.splits += 1
            if (len(points_A)>max): self.splitter(points_A)
            if (len(points_B)>max): self.splitter(points_B)
            
    #need to make a standalone namer
    def namer (self,names):
        '''
        turns your ABABABBB tags into actual names
        
        input: a list of names
        output: [one_of_your_names_picked_randomly] = ([x,y], [x,y], ...)
        
        output is actually a set of tuples
        '''
        used = list()
        groups = dict()
        #for every coordinate
        for c1,t1 in self.tags.items():
            #if that coordinate doesn't have a name from you list
            #and if we haven't used up all the names
            if (t1 not in names) and (len(used)<len(names)):
                this_name = 0
                #pick a random name
                while (not this_name) or (this_name in used):
                    this_name = names[random.randint(0,len(names)-1)]
                #and assign it to every coordinate that shares a tag
                else:
                    this_group = set()
                    for c2,t2 in self.tags.items():
                        if t1==t2:
                            self.tags[c1] = this_name
                            self.tags[c2] = this_name
                            this_group.add(c1)
                            this_group.add(c2)
                    #print("\n{} assigned to {} locations".format(this_name,len(this_group)))
                    #print(this_group)
                    used.append(this_name)
                    groups[this_name] = this_group
            elif len(used)==len(names):
                print("\nAll names used")
                break
        return groups
        
        
        
#OTHER



# def cycle (self):
    # if adv.osc==1: adv.osc=0
    # if adv.osc==0: adv.osc=1     