def pdm(x):
    count = 0
    x = x.casefold()
    x1 = list(reversed(x))
    for i in range(0, len(x)):
        if x[i] == x1[i]:
            count = count + 1
    if count == len(x):
        print("String is Palindrome")
    else:
        print("Not palindrome")


word = input("Enter word: ")
pdm(word)