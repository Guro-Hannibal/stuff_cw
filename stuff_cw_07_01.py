def foo(a):
    return str(max([int(el) for el in a.split()])) + ' ' + str(min([int(el) for el in a.split()]))


print(foo("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# " ".join(x(numbers.split(), key=int) for x in (max, min))
