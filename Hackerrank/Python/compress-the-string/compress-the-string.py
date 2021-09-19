from itertools import groupby

print(" ".join([f"({len(list(g))}, {k})" for k, g in groupby(input())]))
