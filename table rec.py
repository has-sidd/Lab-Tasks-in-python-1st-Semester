def table(n, r = 1):
    if r <= ran:
        print(n, "*", r, "=",n * r)
        table(n, r+1)
    else:
        return

ran = int(input())
table(5)