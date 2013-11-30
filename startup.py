#startup.py
import galaxy as gal
start_galaxy = gal.galaxy_gen()
(x,y) = gal.star_gen.map[16]
print(x,"x",y,"y")
print(gal.get.events(x,y))
print(gal.get.constellation(x,y))
print(gal.get.star_name(x,y))