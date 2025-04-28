# area of circle 
# area = pi * radius * radius 
from math import pi
radius = float(input("Enter radius of circle: "))
def area_of_circle(r):
    return round(pi * r * r,2)
area = area_of_circle(r=radius)
print("Area of the given circle of radius {} units is {} units square".format(radius,area))