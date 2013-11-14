#travel_rest.py
#import as TR

#go to a system, do things. rinse repeat

import ship_state as ship
import pathfinder

jump_to = pathfinder.find(45,145)
print(jump_to.jump_list)
del jump_to