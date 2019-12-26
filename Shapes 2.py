i = 1
j = 1
while i <= 8:
    while j <= 8:
        print("$", end="")
        j += 1
    j = 1
    print()
    i += 1
print()

i = 1
while i <= 8:
    print("$" * i)
    i += 1
print()

i = 1
j = 1
while i <= 8:
    while j <= 8-i:
        print("$", end="")
        j += 1
    j = 1
    print()
    i += 1
print()

i = 0
while i <= 8:
    print(" " * i, "$" * (8-i))
    i += 1
print()

i = 0
while i <= 8:
    print(" " * i, "$" * (8+i))
    i += 1
print()

i = 0
while i <= 8:
    print("$" * i, " " * (8-i))
    i += 1