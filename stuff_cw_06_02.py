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


print(is_prime(73))