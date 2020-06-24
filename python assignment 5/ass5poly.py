#find area of regular polygon
import math
gravity=9.8
len = float(input("enter the side of polygon( meters) :"))
sides = int(input("enter the number of sides:"))
area=(sides*len**2)/(4*math.tan(math.pi/sides))
print("the area of polygon is ",area)