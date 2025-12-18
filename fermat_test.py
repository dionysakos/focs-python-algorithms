import random

def FermatPrime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2:
        return False
    for i in range(0, 30):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

