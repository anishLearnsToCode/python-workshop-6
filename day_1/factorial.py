n = int(input())

# 1 . 2 * 3 * ... * n
# 0! = 1

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(factorial)
