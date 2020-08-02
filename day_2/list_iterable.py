numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# for number in numbers:
#     print(number / 10)

complex = [-9, [], [1, 2, 3], 'hello', True, ['world', 3, range(1, 2)], 90, range(10), 10]

# for element in complex:
#     if isinstance(element, list) or isinstance(element, range) or isinstance(element, str):
#         print(str(element) + ' ' + str(len(element)))

details = [['anish', 90], ['rita', 100], ['john', 80], [], ['john 2', 80]]

for name, marks in details:
    print(name + ' : ' + str(marks))
