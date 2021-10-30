def foo(a):
    count_one = [el for el in str(bin(a).strip('')) if el == '1']
    return len(count_one)


print(foo(1234))
print(foo(4))
print(foo(7))
print(foo(9))
print(foo(10))

# some = lambda n: bin(n).count('1') bad way E731

# print(some(1234))
# print(some(4))
# print(some(7))
# print(some(9))


def count_bits(n):
    return bin(n).count("1")
