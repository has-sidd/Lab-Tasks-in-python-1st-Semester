for i in range(0, 8):
    for j in range(0, 5):
        print("*", end="")
    print()
print()


for i in range(0, 8):
    for j in range(0, 5+i):
        print("*", end="")
    print()
print()


for i in range(0, 8):
    for j in range(0, 5-i):
        print("*", end="")
    print()