

# v0: works
# from collections import namedtuple
# N, scores = int(input()), []
#
# fields = namedtuple('fields',input().split())
# for student in range(N):
#     obj = fields._make(input().split())
#     scores.append(int(obj.MARKS))
#
# print(round(sum(scores)/N,2))

from collections import namedtuple
N, fields = int(input()),namedtuple('fields',input().split())
print(sum([int(fields._make(input().split()).MARKS) for i in range(N)])/N)
