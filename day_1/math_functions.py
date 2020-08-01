def sumNNaturalNumbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def permutation(n, r): #nPr = n! / (n - r)!
    return factorial(n) // factorial(n - r)


def combination(n, r): #nCr = n! / ((n - r)! * r!) = nPr / r!
    return permutation(n, r) // factorial(r)


print(combination(4, 0))
print(combination(4, 1))
print(combination(4, 2))
print(combination(4, 3))
print(combination(4, 4))
