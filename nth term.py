from math import*


def trm(a, d, n):
    x = a + (d*(n-1))
    return x


first = float(input("Enter the fist term : "))
diff = float(input("Enter the common difference : "))
cont = input("Do you want to continue, yes/no : ")
while cont == "yes":
    term = float(input("Enter the number of term to generate : "))
    print("The nth term is : ", trm(first, diff, term))
else:
    print("END")