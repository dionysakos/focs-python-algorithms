m = {0: 0, 1: 1}

def fib1(n, m):
    if n in m:
        return m[n]
    res = fib1(n - 1, m) + fib1(n - 2, m)
    m[n] = res
    return res
