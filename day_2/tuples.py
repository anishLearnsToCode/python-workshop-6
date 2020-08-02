"""
-- they are immutable
-- they cant be changes

()
"""

coordinate = (1, -8, 3)
coordinate1 = (1, -8, 3)
coordinate2 = (1, -8, 3)
coordinate3 = (1, -8, 3)

vowels = ('a', 'e', 'i', 'o', 'u')


def isVowel(character):
    return character in vowels

print(isVowel('a'))
print(isVowel('l'))

position = (2, 5)
car1 = ('honda', 'city', 5, 'reg234234')
car2 = ('maruti', 'alto', 4, 'reg454323')
# print(type(position))
# print(position)

print(car1[1 : 3])
