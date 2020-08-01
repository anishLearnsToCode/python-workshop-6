"""
For Loop

for variable in iterable_object:
    code
"""

r = range(10)
print(type(r))
iterator = r.__iter__()
print(type(iterator))

# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# while True:
#     try:
#         number = iterator.__next__()
#         print(number)
#     except:
#         print('the loop has ended')
#         break


for number in range(10):
    print(number)
