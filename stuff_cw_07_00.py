def foo(a):
    # result = ['Senior' for el in a if (el[0] > 55 and el[1] > 7)]
    # result = []
    # for el in a:
    #     if el[0] > 55 and el[1] > 7:
    #         result.append('Senior')
    #     else:
    #         result.append('Open')
    return ['Senior' if age >= 55 and handi > 7 else 'Open' for age, handi in a]


print(foo([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))

