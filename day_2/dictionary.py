"""
Dictionary / HashMap

list
f : index --> value
    (int)     (anything)
    (unique)  (not unique)

f : anything --> anything
    key     -->  value
    (unique) --> (not unique)

{}
"""

words = {
    'i': 76,
    'am': 100,
    'batman': 9
}

numbers = set()
print(type(numbers))

# print(type(words))
print(words)
words['i'] = 54
print(words)
words['zorro'] = 2
print(words)
del words['batman']
print(words)
print('batman' in words)
words.clear()
print(type(words))
print(words)
