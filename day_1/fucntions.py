"""
Functions

def func_name(argument1, argument2, argument3 ...)
    code
    return value1, value2 ... (not compulsory)
"""


def hello():
    print('hello')


def helloWorld():
    print('hello world')


def fullName(firstName, lastName, middleName=''):
    if middleName:
        print(firstName + ' ' + middleName + ' ' + lastName)
    else:
        print(firstName + ' ' + lastName)


print(type(hello))
# function invocation
# positional arguments
# fullName('anish', 'sachdeva')
# fullName('john', 'doe')
# fullName('wolfgan', 'mozart', 'amadeus')
# fullName(middleName='ada', lastName='countess of lovelace',firstName='lady')
fullName('john', lastName='wick')