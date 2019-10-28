def distance(p1,p2):
	return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def polygon_area(points): # Shoelace Formula
    area=0
    j=n-1
    for i in range(len(points)):
    	area+=(points[j].x+points[i].x)*(points[j].y-points[i].y)
    	j=i
    return abs(area/2)

from collections import namedtuple
Point = namedtuple('Point','x y')

'''
https://en.wikipedia.org/wiki/Shoelace_formula
https://en.wikipedia.org/wiki/Pick%27s_theorem
'''