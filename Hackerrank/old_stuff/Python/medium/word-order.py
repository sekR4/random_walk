
d, w = {}, []
[w.append(input()) for _ in range(int(input()))]

for i in w:
    d[i] = 0

for k in w:
    if k in d.keys():
        d[k] += 1

print(len(d))
print(*d.values())
