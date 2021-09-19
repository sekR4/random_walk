# https://www.hackerrank.com/challenges/re-group-groups/problem
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)


# string = 'hasse'
# m, result = re.findall(r'\w+', string)[0], -1
# for i in m:
#     if m.count(i) > 1 & i.isalnum() == True:
#         result = i
#         break
# print(result)


# m = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@hackerrank.com')
# groups()
# print(m.groups())

# group()
# print(m.group(0))
# print(m.group(3))

# groupdict()
# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)', 'myname@hackerrank.com')
# print(m.groupdict())
