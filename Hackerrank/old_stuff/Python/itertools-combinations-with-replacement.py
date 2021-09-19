from itertools import combinations_with_replacement

s,k = input().split()
# print(*[''.join(list(i)) for i in sorted(combinations_with_replacement(s,int(k)))],sep='\n')
print(*[''.join(list(i)) for i in combinations_with_replacement(sorted(s),int(k))],sep='\n')
