number = int(input())
# number! = 1 * 2 * 3 * .. * number

factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i

print(factorial)
