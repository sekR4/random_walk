# my solution (works)
# n,s = int(input()),set()
#
# for i in range(n):
#     s.add(input())
#
# print(len(s))

# best practice?
print(len({input() for x in range(int(input()))}))
