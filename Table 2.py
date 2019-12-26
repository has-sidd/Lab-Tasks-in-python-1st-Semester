def table(y):
    for i in range(1, 10):
        ans = y * table(i-1)
        return ans
