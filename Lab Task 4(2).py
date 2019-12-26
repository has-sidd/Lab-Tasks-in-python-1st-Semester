#Q2
a = float(input("Enter the fist term : "))
d = float(input("Enter the common difference : "))
cont = input("Do you want to continue, yes/no : ")
while cont == "yes":
    n = float(input("Enter the number of term to generate : "))
    x = a + (d*(n-1))
    print("The nth term is : ", x)
else:
    print("END")