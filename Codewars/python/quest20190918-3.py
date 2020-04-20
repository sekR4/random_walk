# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python
# names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
#
# test.assert_equals(who_is_next(names, 1), "Sheldon")
# test.assert_equals(who_is_next(names, 52), "Penny")
import math
# names = ['1','2','3','4']
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
def who_is_next(names, r):
    # your code
    # if r <= len(names):
    #     idx = r-1
    #     # print(names[r-1])
    # else:
    # idx = r - (r/len(names))**2
    #     # print('ha')
    #     # print()
    #     # print(names[len(names)-r+1])
    # # print(names[idx])
    #
    # print('idx: {} '.format(idx),
    #       # 'idx/len(names): {}'.format(idx/len(names)),
    #       'r/len(names): {}'.format(r/len(names)))
    # print(len(names)/r, (r - r/len(names))*len(names)/r)
    # lst = names*(math.ceil(r/len(names)))
    print((names*(math.ceil(r/len(names))))[r-1])

import math
def who_is_next(names, r):
    if (r % 2) != 0:
        return (names*(math.ceil(r/len(names))))[r-1]
    return (names*(math.ceil(r/len(names))))[r]

print(who_is_next(names,4))
print(who_is_next(names, 1) == "Sheldon")
print(who_is_next(names, 52) == "Penny")
# print(who_is_next(names, 7230702951) == "Leonard")



# import itertools

# print(itertools.chain.from_iterable(itertools.repeat(names, 5)))
# itertools.chain(it1, it2)
# print(itertools.cycle(names)[0])
# itertools.chain.from_iterable(names*

# print(names*floor(3/4))
# print(math.ceil(3/4))
