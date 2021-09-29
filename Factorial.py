def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(10)) # should return 24
print(factorial(5)) # should return 120


# print the first 10 factorials (from 0 to 9) with the corresponding number.

for n in range(0,10):
    print(n, factorial(n+1))