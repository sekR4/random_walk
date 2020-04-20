# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python
# find_missing([1, 3, 5, 9, 11]) == 7

def find_missing(lst):
    dff = [j-i for i, j in zip(lst[:-1], lst[1:])]
    mode = max(set(dff), key=dff.count)
    for i in range(len(dff)):
        if dff[i] != mode:
            idx = i + 1
    lst0 = lst[:idx]
    print(lst0[-1] + mode)
    return lst0[-1] + mode

    # lst0.append(lst0[-1] + max(set(dff), key=dff.count))
    # print(lst0+lst[idx:])
    # return lst0+lst[idx:]

def find_missing_best_practice(sequence):
    # t = sequence
    # print('t[0]: ', t[0])
    # print('t[-1]: ', t[-1])
    # print('(t[0] + t[-1]): ', (t[0] + t[-1]))
    # print('len(t) + 1: ', len(t) + 1)
    # print('sum(t)',sum(t))
    # print((t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t))
    return (sequence[0] + sequence[-1]) * (len(sequence) + 1) / 2 - sum(sequence)

find_missing([2,4,8])
# find_missing_best_practice([2,4,8])
# print(lst0)
#
# print(lst[idx:])

# print(lst0+lst[idx:])
# print(i)
# print(lst0[-1])
# print(max(set(dff), key=dff.count)) #mode
# print(dff)
#
# for i in range(len(lst)):
#     print(i,lst[i])

# for number in list(set(dff)):
#     print(number, dff.count(number))

# print(dff.count(4))
# print(list(set(dff)))

# import numpy as np
# print(np.diff(lst))

# print([j-i for i, j in zip(lst[:-1], lst[1:])])
#
# print(lst[:-1],lst[1:])
# print(zip(lst[:-1], lst[1:]))
#
# for i,j in zip(lst[:-1], lst[1:]):
#     print(j,i)
#     print(j-i)
