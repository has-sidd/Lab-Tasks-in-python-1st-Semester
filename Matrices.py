a = [[4,5],[0.-7]]
b = [[1,-9],[1,-1]]
x = [[0,0],[0,0]]
if len(a) == len(b):
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            x[i][j] = a[i][j] + b[i][j]
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            print(x[i][j], end="  ")
        print()
else:
    print("not 2*2 matrice")
