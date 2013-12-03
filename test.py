import lynn_custom as LC
import random

test_map = dict()
r = 85
for x in range(r):
    for y in range(r):
        test_map[x,y] = random.gauss(50,10)

LC.aggregrate(test_map,r,r)