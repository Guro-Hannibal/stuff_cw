def foo(a=''):
    str_lower = a.lower()
    result = ''
    i = 0
    while i < len(str_lower):
        result += str_lower[i].upper()
        j = 0
        while j < i:
            result += str_lower[i]
            j += 1
        i += 1
        if i != len(str_lower):
            result += '-'
    return result


print(foo('ZpglnRxqenU'))

# return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# return '-'.join((a * i).title() for i, a in enumerate(s, 1))
