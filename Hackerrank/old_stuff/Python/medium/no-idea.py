
# testing
_, n = '3 2', '1 5 3'.split()
A, B = set('3 1'.split()), set('5 7'.split())

print(sum([(i in A) - (i in B) for i in n]))

# refactored submission
_, n = input(), input().split()
A, B = set(input().split()), set(input().split())
print(sum([(i in A) - (i in B) for i in n]))
