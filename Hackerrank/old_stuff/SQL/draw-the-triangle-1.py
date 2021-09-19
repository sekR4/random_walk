p = 20
# print('select\n')
# for i in range(p):
#     print("\'"+(p-i)*'*'+"\'" + ",\n")
# print('from dual;')

# print('select')
out = 'select '
for i in range(p):
    out += "\'"+(p-i)*'*'+"\'"
    if i < (p-1):
        out += ","
    else:
        out += ' '
    # print("\'"+(p-i)*'*'+"\'" + ",\n")
out += 'from dual;'
print(out)
