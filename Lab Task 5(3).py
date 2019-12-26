# b)
i = 1
while i <= 8:
    print("*" * i)
    i += 1
print()
# c)
i = 1
j = 1
while i <= 8:
    while j <= 8-i:
        print("*", end="")
        j += 1
    j = 1
    print()
    i += 1