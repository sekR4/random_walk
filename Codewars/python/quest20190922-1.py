# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

n = 53100
n = str(n)
n = list(n)

# for i in
zahl = []
for i in range(len(n)-1):
    print('i: {}'.format(i),'reverse indexed n: ', n[(i+1)*(-1)])
    print('i: {}'.format(i),'reverse indexed n-1: ', n[(i+2)*(-1)], '\n')
    # print('(i+1)*(-1): ',(i+1)*(-1))
    # print('n[(i+2)*(-1)]: ',(i+2)*(-1), '\n')

    if n[(i+1)*(-1)] < n[(i+2)*(-1)]:
        print(n[(i+1)*(-1)],n[(i+2)*(-1)])
        print(n[:(i+2)*(-1)],[n[(i+1)*(-1)],n[(i+2)*(-1)]])
        break
    # zahl.append(n[(i+1)*(-1)])
    # zahl.append(n[(i+2)*(-1)])
print(zahl)
