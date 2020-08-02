"""
Generators
{ x^2 | x is a natural number}
{ x^2 | 1 <= x <= 8 }
{ 5x | x is an integr}

(generator(x) for x in iterable)
--> generators are iterable
"""

n = int(input())
odd_even = list([number, 'even' if number % 2 == 0 else 'odd'] for number in range(0, n + 1))
print(odd_even)

# n = int(input())
# naturalNumbers = list(number for number in range(1, n + 1))
# print(naturalNumbers)
