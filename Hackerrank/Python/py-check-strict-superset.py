# my solution worked
# A = set(input().split())
# if sum([1 for i in range(int(input())) if A.issuperset(set(input().split())) == False]) > 0:
#     print('False')
# else:
#     print('True')

# this is a shorter one provided by aportnoy1
# a = set(input().split())
# print(all(a > set(input().split()) for _ in range(int(input()))))
# The all() function returns True if all items in an iterable are true, otherwise it returns False.

# Modifiziert:
A = set(input().split())
print(all(A.issuperset(set(input().split())) for _ in range(int(input()))))
