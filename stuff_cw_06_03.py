def who_like_this(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


print(who_like_this([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def likes(names):
    length = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, length)].format(*names[:3], others=length-2)


print(likes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

