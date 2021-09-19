import re

def regexp_substr(string,pattern):
    """ Takes 2 strings as input.
        Returns None when pattern not found. """
    p=re.compile(pattern)
    try: out = p.findall(string)[0]
    except: out = None
    return out


n = int(input())

contacts = {}

for i in range(n):
    name,number = input().split()
    contacts['{}'.format(name)] = regexp_substr(number,'\d+')

# for i in range(n):
#     query = input()
#     if query in contacts:
#         print('{}={}'.format(query,contacts[query]))
#     else:
#         print('Not found')

while True:
    try:
        name = input()
        if name in contacts:
            print(name, "=", contacts[name], sep="")
        else : print("Not found")
    except: break
