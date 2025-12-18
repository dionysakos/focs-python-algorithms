def bgcd(a, b):
    if a == b:
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * bgcd(a // 2, b // 2)
    elif a % 2 == 0 and b % 2 != 0:
        return bgcd(a // 2, b)
    elif a % 2 != 0 and b % 2 == 0:
        return bgcd(a, b // 2)
    else:
        return bgcd(min(a, b), abs(a - b) // 2)
