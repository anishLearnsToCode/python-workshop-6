complex = {
    'hello': 'world',
    1: 10,
    'pi': 3.14,
    10.67: 'number',
    range(10): {
        'numbers': [1, 2, 3],
        'even': [2, 4, 6],
        'prime': [2, 3, 5, 7]
    },
    'online': True,
    'list': range(1, 2, 2)
}

# print(complex['list'])

values = complex.values()
# print(type(values))

# for value in complex.values():
#     print(value)

# for key in complex.keys():
#     print(key)

for key, value in complex.items():
    print(str(key) + ' : ' + str(value))