n = int(input())
scores = list(map(int, input().split()))
print(max([x for x in scores if x < max(scores)]))
