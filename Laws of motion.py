def one(u, a, t):
    v = u + (a*t)
    print("Velocity is : ", v, "m/s")


def two(u, a, t):
    s = (u*t) + (1/2)*(a)*(t**2)
    print("Displacement is : ", s, "m")


def third(u, v, a):#2as = v2 - u2
    s = ((v**2) - (u**2))/ 2 * (a)
    print("Distance is : ", s, "m")


u = float(input("Enter initial Velocity : "))
a = float(input("Enter acceleration : "))
t = float(input("Enter time : "))
one(u, a, t)
two(u, a, t)
v = float(input("Enter final Velocity : "))
third(u, v, a)