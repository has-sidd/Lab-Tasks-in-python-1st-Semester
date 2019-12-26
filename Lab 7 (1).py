list1 = [(5, 3), (5,8), (6.2, 5.7), (1.1, 8), (3,7)]
minimum = min(list1)
maximum = max(list1)
print("Minimum Tuple is : {0} and Maximum Tuple is : {1}".format(minimum,maximum))

print()

co = [(1,1), (10,11), (6,6), (7,8)]
for i in co:
    x = 0
    y = 1
    if i[x] <= 10 and i[y] <= 10:
        print(i, "True")
    else:
        print(i, "False")