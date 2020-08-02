def swapCase(string):
    accumulator = ''
    for character in string:
        if character.isupper():
            accumulator += character.lower()
        else:
            accumulator += character.upper()
    return accumulator


print(swapCase('hello world'))
# HELLO WORLD

print(swapCase('John Doe'))
# jOHN dOE
