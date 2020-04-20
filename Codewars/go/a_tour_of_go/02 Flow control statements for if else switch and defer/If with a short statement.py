def pow(x, n, lim):
    v = x**n
    if v < lim:
        return v
    else:
        return lim


print(pow(3, 2, 10), pow(3, 3, 10))
