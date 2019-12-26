from math import*


def area(r, h):
    x = (2*pi*r*h) + (2*pi*(r**2))
    return x


def volume(r, h):
    x = (pi*r**2)*h
    return x


radius = float(input("Enter radius of cylinder : "))
height = float(input("Enter height of cylinder : "))
if radius <= 0 or height <= 0:
    print("INVALID INPUT")
else:
    print("The area of cylinder is : ", area(radius, height))
    print("The volume of cylinder is : ", volume(radius, height))   