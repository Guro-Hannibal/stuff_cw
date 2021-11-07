import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for dev in range(2, int(math.sqrt(num)) + 1):
        if num % dev == 0:
            return False
    return True


def is_prime_1line(num):
    return num > 1 and all(num % dev for dev in range(2, int(math.sqrt(num)) + 1))


def test(num):
    result = [all(num % dev for dev in range(2, int(math.sqrt(num)) + 1))]
    return result


print(is_prime(73))

print(is_prime_1line(73))

print(test(70))
