a = "anachronistically"
b = "counterintuitive"
a = len(a)
b = len(b)
x = a - b
print(x)

print()
x1 = "misinterpretation"
x2 = "misrepresentation"
if ascii(x1[3]) < ascii(x2[3]):
    print(x1, "Comes first in Dictionary")
else:
    print(x2, "Comes first in Dictionary")