from math import*
data = [[54,8],[5,2],[24,58],[24,8]]
for x in range(len(data)):
    h = round(data[x][0]*sin(radians(data[x][1])), 2)
    print("Length of ladder is : ", data[x][0])
    print("Angle with ground is:", data[x][1])
    print("height reached by ladder is :", h)