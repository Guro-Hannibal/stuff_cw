def spin_words(sentence):
    list_demo = [el for el in sentence.split()]
    result = []
    for item in list_demo:
        if len(item) > 5:
            result.append(''.join(reversed(item)))
        else:
            result.append(item)
    return ' '.join(result)


# return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

print(spin_words('Write gnirts is or name will be etirW gnirts is or name will be'))

str1 = 'wololo'

print(''.join(str1[::-1]))
