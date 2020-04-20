i,M = int(input()), set(list(map(int,input().split())))
i,N = int(input()), set(list(map(int,input().split())))
print(*sorted(M.symmetric_difference(N)),sep='\n')
