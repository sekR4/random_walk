_, s = input(), input().split()
print(all(int(i) > 0 for i in s) and any(j == j[::-1] for j in s))
