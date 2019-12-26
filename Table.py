from math import*


def table(x):
    print(" " * 13, "Sin", " " * 21, "Cos", " " * 18, "Tan")
    for i in range(x):
        sn = sin(i+1)
        cs = cos(i+1)
        tn = tan(i+1)
        print(i+1, ":", " ", sn, "\t", " ", cs, "\t", " ", tn)


Angle = int(input("Enter the range of Angles : "))
table(Angle)