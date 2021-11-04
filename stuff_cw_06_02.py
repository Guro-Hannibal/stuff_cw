def is_prime(num):
    result = True
    if num < 0:
        return False
    elif num == 1 or num == 0:
        return False
    for dev in range(2, num):
        if num % dev == 0:
            print(num, dev)
            result = False
    return result


print(is_prime(0))
