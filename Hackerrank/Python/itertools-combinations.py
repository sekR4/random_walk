from itertools import combinations

s,k = input().split()
for i in range(1,int(k)+1):
    print(*[''.join(list(i)) for i in combinations(sorted(s),i)],sep='\n')
