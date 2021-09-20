from itertools import combinations

n, l, k = int(input()), input().replace(" ", ""), int(input())
combos = ["".join(i) for i in combinations(l, k)]
sum_a = sum([s.count("a") > 0 for s in combos])

print(round(sum_a / len(combos), 4))
