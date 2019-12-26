def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact*i
    return fact


result = int(input("Enter Number : "))
print("Answer is :", factorial(result))