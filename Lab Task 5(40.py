def factorial(x):
    if x == 1 or x == 0:
        return x
    else:
        return x*factorial(x-1)


i = 0
while i <= 10:
    print(i,"!", factorial(i))
    i += 1