def fib_k(n, k):
    fib = FibMat(n)
    res = fib % (pow(10, k))
    return res
