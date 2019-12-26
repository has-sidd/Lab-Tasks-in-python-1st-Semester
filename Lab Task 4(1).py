#Q1
from math import*
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))
if a == 0:
    print("Equation can not be solved")
else:
    d = (b**2)-(4*a*c)
    sol1 = (-b + sqrt(d))/(2*a)
    sol2 = (-b - sqrt(d))/(2*a)
    print("The solutions are {0} and {1}".format(sol1, sol2))