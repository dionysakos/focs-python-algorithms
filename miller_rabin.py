import random

def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2:
        return False
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for i in range(0, 30):
        if MillerRabin(n, d) == False:
            return False
    return True


def MillerRabin(n, d):
    a = random.randint(2, n - 1)
    res = pow(a, d, n)

    if res == 1 or res == n - 1:
        return True

    while d != n - 1:
        res = pow(res, 2, n)
        d *= 2
        if res == 1:
            return False
        elif res == n - 1:
            return True

    return False
