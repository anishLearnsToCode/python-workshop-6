def frequency(sentence):
    result = {}
    for word in sentence.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


print(frequency(''))
print(frequency('i am batman'))
print(frequency('i am i surely am i am proven to be batman. i really am'))
