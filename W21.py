def rotatelist(l, n):
    if len(l) < n:
        n = n % len(l)
    if n > 0:
        l = l[n:] + l[:n]
    elif n < 0:
        l = l[-n:] + l[:-n]
    return l
