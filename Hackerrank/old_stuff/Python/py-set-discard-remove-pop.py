# n = int(input())
# s = set(map(int,input().split()))
# N = int(input())
#
# for c in range(N):
#     cmd = input().split()
#     if len(cmd) == 1: eval('s.' + cmd[0] + '()')
#     else: eval('s.' + cmd[0] + f'({int(cmd[1])})')
#
# print(sum(s))

#best solution:
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))
