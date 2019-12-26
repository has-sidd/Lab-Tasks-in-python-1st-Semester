num = int(input("Enter any number : "))
if num < 0:
    print("Invalid Number")
for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        break

else:
    print("prime number")