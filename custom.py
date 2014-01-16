#custom.py

import sys
import math
import random
import time
import csv
import numpy

def rotate (point_x, point_y, rads, center=(0,0)):
    newX = center[0] + (point_x-center[0])*math.cos(rads) - (point_y-center[1])*math.sin(rads)
    newY = center[1] + (point_x-center[0])*math.sin(rads) + (point_y-center[1])*math.cos(rads)
    return newX,newY

def create_distance_matrix (size):
    distance_matrix = dict()
    for x1 in range(size):
        for y1 in range(size):
            distance_matrix[x1, y1] = numpy.empty((size, size))
            for (x2, y2), dont_need in numpy.ndenumerate(distance_matrix[x1, y1]):
                distance_matrix[x1, y1][x2, y2] = (math.hypot(x1-x2, y1-y2)
    return distance_matrix

def sortkeys (data):
    out = list()
    for entry in data.keys(): out.append(entry)
    return sorted(out)

def proceed (text):
    go = input(text+" ")
    while not go == "yes":
        if go == "no":
            sure = input("WAIT WAIT ARE YOU SURE??? [yes/no] ")
            if sure == "yes": sys.exit()
        go = input(text+" [yes/no] ")

def make_sphere (r): 
    inr = set()
    for x in range(r+1):
        for y in range(r+1):
            if math.hypot(x,y)<=r:
                inr.add((x,y))
                inr.add((-x,y))
                inr.add((x,-y))
                inr.add((-x,-y))
    dmap = dict()
    for x,y in inr:
        dmod = r+1-math.hypot(x,y)
        dmap[x,y] = dmod
    return dmap

def write_to_chart (collection,h,v,filename):
    '''
    input: dictionary [x,y]=val or list [(x,y),(x,y)...], 
    horizontal, verticle, your_file.csv
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
        else: print("\nInvalid type\n")

def y_dict_sort (dic):
    '''
    sorts a dictionary by its values
    
    input: dictionary
    output: list(key,key,key...)
    '''
    dlist = list()
    for (k,v) in dic.items(): dlist.append((v,k))
    dlist.sort()
    out = list()
    for (a,b) in dlist: out.append(b)
    return out  

def values_to_list (dic):
    '''not sure that I even need this'''
    v_list = list()
    for i in dic.values(): v_list.append(i)
    return v_list
 
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
    except IndexError: print("\nERROR: percentile ratio not valid\n")

def get_percentile (values,number):
    '''gets the "percentile" of a given number within a list'''
    values.sort
    place = values.index(number)
    return (place/len(values))
    
def rampfunc (x1,x2,y1,y2,x):
    '''applies a ramp function'''
    if x1<=x<=x2:
        m = (y1-y2)/(x1-x2)
        b = y1 - m*x1
        y = m*x+b
        return y
    elif x1>x: return y1
    elif x>x2: return y2

def linear_rescale (x1,x2,y1,y2,x):
    '''
    scales a value according to a linear function
    input: x1,x2,y1,y2
    '''
    m = (y1-y2)/(x1-x2)
    b = y1 - m*x1
    y = m*x+b
    #print(x1,x2,y1,y2," m ",m," b ",b)
    return y
    
def perpendicular_eq (m,x,y):
    p_m = -(1/m)
    p_b = y-p_m*x
    return (p_m,p_b)
    
def find_center (inp):
    point = [0,0]
    x_list = list()
    y_list = list()
    for (x,y) in inp:
        x_list.append(x)
        y_list.append(y)
    point[0] = average(x_list)
    point[1] = average(y_list)
    point = tuple(point)
    return point    

def c_o_m (data):
    t_mass = 0
    w_pos = [0,0]
    for k,v in data.items():
        x = k[0]
        y = k[1]
        mass = v["mass"]
        t_mass += mass
        w_pos[0] += x*mass
        w_pos[1] += y*mass
    if t_mass:
        x = round(w_pos[0]/t_mass)
        y = round(w_pos[1]/t_mass)
        center = [x,y]
        return center,t_mass
    else: return [0,0],0
    
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
  
def to_base(num,base):
    #dividend
    d = list()
    d.append(num)
    #remainder
    r = list()
    conv = list()
    string = str()
    letters = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G",17:"H",18:"I",19:"J"}
    while (d[-1]>=base):
        r.append(d[-1]%base)
        d.append(d[-1]//base)
    if d[-1]>=10:
        conv.append(letters[d[-1]])
    else:
        conv.append(d[-1])
    for var in range(len(r)):
        if r[-1]>=10:
            conv.append(letters[r.pop()])
        else:
            conv.append(r.pop())
    for entry in conv:
        string += str(entry)
    return string

class clusters (object):  
    '''
    elucidian distance hierichal
    clustuer function (top -> bottom)
    splits into boxes
    
    input: a list of (x,y) tuples
    output: [x,y] = "XXXXXX"
    
    "XXXXXX" is the split history. example: ABBBAB
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
                print("\nAll names used\n")
                break
        return groups