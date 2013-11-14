#pathfinder.py
#import as pathfinder

#plots your path through space

import math
import galaxy as gal
import lynn_custom as LC
import ship_state as ship
FTL = ship.subsystem.FTL
loc = ship.location

class find (object):
    def __init__ (self,col_x,col_y):
        #call this
        self.jump_list = list()
        cur_x = loc.x
        cur_y = loc.y
        #colony path m, colony path b
        (cp_m,cp_b) = LC.linear_eq(cur_x,cur_y,col_x,col_y)
        #corner points
        corner_x = cur_x+1
        corner_y = cp_m*corner_x+cp_b
        #perpendicular m, perpendicular b
        (p_m,p_b) = LC.perpendicular_eq(cp_m,corner_x,corner_y)
        #adjacent
        adj = LC.dist_2d(cur_x,cur_y,corner_x,corner_y)
        #half accuracy point, REALLY SHOULDN'T jump past this
        hap = (FTL.o_dist**2)/(4*FTL.b_iacc)+FTL.o_dist/2
        #no accurary point, CAN'T jump past this
        nap = (FTL.o_dist**2)/(2*FTL.b_iacc)+FTL.o_dist/2
        #get nearby stars
        nearby = list()
        in_range = list()
        for star_x,star_y in gal.star_gen.map:
            range_to = LC.dist_2d(cur_x,cur_y,star_x,star_y)
            if (range_to<hap):
                nearby.append((star_x,star_y))
            elif (range_to<nap):
                in_range.append((star_x,star_y))
        def check_angle (to_check):
            in_angle = list()
            for star_x,star_y in to_check:
                if cur_x==star_x:
                    p_int_x = cur_x
                else:
                    try:
                        (star_m,star_b) = LC.linear_eq(cur_x,cur_y,star_x,star_y)
                        p_int_x = (star_b-p_b)/(p_m-star_m)
                    #this is the star is perpendicular to colony path condition
                    except ZeroDivisionError:
                        continue 
                p_int_y = p_m*p_int_x+p_b
                hyp = LC.dist_2d(cur_x,cur_y,p_int_x,p_int_y)
                if math.acos((adj/hyp))<0.25*math.pi:
                    in_angle.append((star_x,star_y))
            return in_angle
        def check_backw (to_check):
            checked = list()
            for pos_x,pos_y in to_check:
                cur_new = LC.dist_2d(cur_x,cur_y,pos_x,pos_y)
                old_new = LC.dist_2d(cur_x-1,cur_y-1,pos_x,pos_y)
                if old_new>cur_new:
                    checked.append((pos_x,pos_y))
            return checked
        c_a = check_angle(nearby)
        c_b = check_backw(c_a)
        if len(c_b)<4:
            print("running extended scan")
            c_a = check_angle(in_range)
            c_b = check_backw(c_a)
        self.jump_list = c_b.copy()