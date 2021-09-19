n_elements = int(input())
lst = list(map(int, input().split()))

# strg='3 7 8 5 12 14 21 13 18'
# print(list(map(int, strg.split())))
#
# n_elements = 9
# lst = [3, 7, 8, 5, 12, 14, 21, 13, 18]
lst=sorted(lst)

from statistics import median
print(int(median(lst[:n_elements//2])))
print(int(median(lst)))
print(int(median(lst[(n_elements+1)//2:])))
