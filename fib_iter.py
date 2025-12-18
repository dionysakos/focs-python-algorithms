def fib2(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(1, n):
        c = b
        b = a + b
        a = c
    return b
