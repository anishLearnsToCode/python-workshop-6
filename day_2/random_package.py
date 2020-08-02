import random


def randomInteger(a, b):
    return int((b - a) * random.random() + a)


print(random.randint(0, 100))
print(random.randint(10, 20))
print(random.randint(900, 1000))
