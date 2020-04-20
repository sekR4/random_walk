from statistics import pstdev
n = int(input())
x = list(map(int, input().split()))
print(round(pstdev(x),1))
