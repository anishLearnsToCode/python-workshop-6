def abs(number):
    return -number if number < 0 else number


def all(iterable):
    for element in iterable:
        if not bool(element):
            return False
    return True


def any(iterable):
    for element in iterable:
        if bool(element):
            return True
    return False


# print(abs(10))
# print(abs(-5))
print(all([]))
print(all(''))
print(all(range(0)))
print(all([True, True, 1, 2, 2, 2, 2, True, 'hello world']))
