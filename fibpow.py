import math

phi = 1.6180339

def fib(n):
    res = pow(phi, n) / math.sqrt(5)
    return round(res)
