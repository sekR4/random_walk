n = int(input())
lst = []

for i in range(n):
    arg = input().split()
    if arg[0] == 'insert': lst.insert(int(arg[1]),int(arg[2]))
    if arg[0] == 'print': print(lst)
    if arg[0] == 'remove': lst.remove(int(arg[1]))
    if arg[0] == 'append': lst.append(int(arg[1]))
    if arg[0] == 'sort': lst.sort()
    if arg[0] == 'pop': lst.pop()
    if arg[0] == 'reverse': lst.reverse()
