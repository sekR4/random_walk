# Testinput
# ns = ['a','a','b','a','b']
# ms = ['a','b']
# n, m = map(int,'5 2'.split())

# print(n,m)

# from collections import defaultdict
# d = defaultdict(list)
# print(d)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# print(d)

# d2 = {}
# d2['python'],d['something-else'] = [],[]
# print(d2)
# d2['python'].append("awesome")
# d2['something-else'].append("not relevant")
# d2['python'].append("language")

# for i in d2.items():
#     print(i)

# trial 1
# A, B = [],[]
#
# for i in range(n):
#     A.append(ns[i])
#
# for i in range(m):
#     B.append(ms[i])
#
# # print(A,B, sep='\n')
#
# for j in range(n):
#     for i in range(m):
#         if B[j] == A[i]:
#             print(i)

# trial 2
# from collections import defaultdict
# d = defaultdict(list)

# for i in range(n):
#     d['A'].append(ns[i])

# for i in range(n):
#     d[ns[i]].append(str(i+1))
#
# for i in range(m):
#     b = ms[i]
#     if b in d: print(' '.join(d[b]))
#     else: print(-1)

# for i in range(m):
#     d['B'].append(ms[i])

# print(*d.items(),sep='\n')

# print(set(d['A']).intersection(d['B']))

# final with raw input
from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(list)
for i in range(n): d[input()].append(str(i+1))

for i in range(m):
    b = input()
    if b in d: print(' '.join(d[b]))
    else: print(-1)
