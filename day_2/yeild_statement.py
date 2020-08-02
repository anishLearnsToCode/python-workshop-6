def print_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


# for number in print_even([1, 2, 3, 4, 5, 6, 7, 2, -100, 0]):
#     print(number)

numbers = [1, 2, 3, 4, 5, 6, 7, 2, -100, 0]
print(list(print_even(numbers))[::-1])
