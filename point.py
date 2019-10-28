from collections import namedtuple
from math import sqrt
'''Point'''
Point = namedtuple('Point', 'x y')
p1 = Point(1.0, 5.0)
p2 = Point(2.5, 1.5)

def distance(p1,p2):
	return sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

def slope(p1,p2):
	if p1.x==p2.x:
		return float('inf')
	return (p2.y-p1.y)/(p2.x-p2.x)

'''Rectangle'''
Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')
ra = Rectangle(3., 3., 5., 5.)
rb = Rectangle(1., 1., 4., 3.5)

'''Circle'''
Circle = namedtuple('Circle','c r')
c1 = Circle(Point(0,0),2)
def circle_area(c):
	return 3.14*c.r*c.r
print(circle_area(c1))