#lynn_custom.py
#import as LC

#a collection of all my personal functions

#todo:
#slanted split
#better averaging and cluster functions
#standard deviation
#oscillator
#significant figures rounder
import math
import random
import time
import csv
#######
# I/O #
#######
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
################    
# DICTIONARIES #
################            
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
    return y

def linear_eq (x1,y1,x2,y2):
    '''gets a linear equation from a set of x,y points'''
    m = (y1-y2)/(x1-x2)
    b = y1 - m*x1
    return (m,b)

def quadratic_rescale():
    pass
    
def perpendicular_eq (m,x,y):
    p_m = -(1/m)
    p_b = y-p_m*x
    return (p_m,p_b)
    
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
def ramp(x):
    if 0<=x<=1.3:return 0.615*x+0.5
    elif 0>x: return 0.5
    elif x>1.3: return 1.3
def aggregrate (grid,grid_x,grid_y,r=5):
    t_grid = grid.copy()
    xrs = set()
    for x in range(r+1):
        for y in range(r+1):
            if math.hypot(x,y)<=r:
                xrs.add((x,y))
                xrs.add((-x,y))
                xrs.add((x,-y))
                xrs.add((-x,-y))
    xrs = list(xrs)
    #
    ystp = [(x,y+1) for (x,y) in xrs]
    yal = [p for p in ystp if p not in xrs]
    yrl = [p for p in xrs if p not in ystp]
    #
    xstp = [(x+1,y) for (x,y) in xrs]
    xal = [p for p in xstp if p not in xrs]
    xrl = [p for p in xrs if p not in xstp]
    #
    pil = dict()
    for (dx,dy) in xrs:
        try: pil[dx,dy] = grid[dx,dy]
        except KeyError: pass
    for x in range(grid_x):
        xil = pil.copy()
        for y in range(grid_y):
            pl = len(pil)
            s1 = 0
            for v in pil.values(): s1+=v
            ave = s1/pl
            s2 = 0
            for (dx,dy) in pil: s2+=grid[dx,dy]*ramp(grid[dx,dy]/ave)
            t_grid[x,y] = grid[x,y]*ramp(grid[x,y]/ave)*s1/s2
            #step y
            for px,py in yrl:
                try: del pil[x+px,y+py]
                except KeyError: pass
            for px,py in yal:
                try: pil[x+px,y+py] = grid[x+px,y+py]
                except KeyError: pass
        #step x
        for px,py in xrl:
            try: del xil[x+px,py]
            except KeyError: pass
        for px,py in xal:
            try: xil[x+px,py] = grid[x+px,py]
            except KeyError: pass
        pil = xil.copy()
    print("count: ",count)
    grid = t_grid.copy()
    return grid
    
   

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
# def cycle (self):
    # if adv.osc==1: adv.osc=0
    # if adv.osc==0: adv.osc=1     
