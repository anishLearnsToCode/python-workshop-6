"""
Lists / Array
- iterable object
- mutable (it can b changed)

- string is immutable
- range is immutable

[]
"""

numbers = []
print(type(numbers))
print(numbers)

# add elements in the list
# append(value) --> appends element at the end of list
# insert(index, value) --> insert value at index in the list

# removing values
# pop() --> @return last value in list and also remove last value
# pop(index) remove value at particular index in list
# remove(value) --> remove that value from list
# del keyword

numbers = [2, True, False, 'hello world', [1, 2, 3], [], range(1, 10, 3), range(0, 100)]
for x in numbers[6]:
    print(x)
