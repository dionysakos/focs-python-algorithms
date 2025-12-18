prime = [True for i in range(201)]
p = 2

while p * p <= 200:
    if prime[p] == True:
        for j in range(p * p, 201, p):
            prime[j] = False
    p = p + 1

for m in range(2, 200):
    if prime[m] == True:
        mrs = pow(2, m) - 1
        print(mrs)
