name = input("Enter you name : ")
num = len(name)
for i in range(num, 0, -1):
    print(name[i-1], end="")