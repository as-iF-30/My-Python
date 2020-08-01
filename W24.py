def prime(d):
    c = 0
    for i in range(2, d):
        if d % i == 0:
            c += 1
    if c == 0:
        return c
    else:
        return c


def primepartition(n):
    if n == 1 or n == 2 or n == 3:
        return False
    j = 2
    b = 0
    while j <= n - j:
        if prime(j) == 0 and prime(n - j) == 0:
            return True
        else:
            b += 1
        j += 1
    if b != 0:
        return False
