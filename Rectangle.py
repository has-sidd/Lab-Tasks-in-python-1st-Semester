from math import*


def area(l, w):
    x = l * w
    return x


length = float(input("Enter length of rectangle : "))
width = float(input("Enter width of rectangle : "))
print("The area of rectangle is : ", area(length, width))