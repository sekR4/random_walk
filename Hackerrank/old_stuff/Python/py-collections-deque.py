from collections import deque
d = deque()
for i in range(int(input())):
    eval('d.{0}({1})'.format(*input().split()+['']))
print(*d,sep=' ')
