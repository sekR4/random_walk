# Works fine for the small test case, but not with unlimited input
# _, n = input(), input().split()
# print(*[i for i in n if n.count(i) == 1])

# sets suggested by itsbruce
# k, n = int(input()), list(map(int, input().split()))
# # list_set = set(n)
# # unique_list = (list(list_set))
# # for x in unique_list:
# #     print(x)
#
# # Python3 code to find the element that
# # appears once
#
#
# def getSingle(arr, n):
#     ones = 1
#     twos = 0
#
#     for i in range(n):
#         # one & arr[i]" gives the bits that
#         # are there in both 'ones' and new
#         # element from arr[]. We add these
#         # bits to 'twos' using bitwise OR
#         twos = twos | (ones & arr[i])
#
#         # one & arr[i]" gives the bits that
#         # are there in both 'ones' and new
#         # element from arr[]. We add these
#         # bits to 'twos' using bitwise OR
#         ones = ones ^ arr[i]
#
#         # The common bits are those bits
#         # which appear third time. So these
#         # bits should not be there in both
#         # 'ones' and 'twos'. common_bit_mask
#         # contains all these bits as 0, so
#         # that the bits can be removed from
#         # 'ones' and 'twos'
#         common_bit_mask = ~(ones & twos)
#
#         # Remove common bits (the bits that
#         # appear third time) from 'ones'
#         ones &= common_bit_mask
#
#         # Remove common bits (the bits that
#         # appear third time) from 'twos'
#         twos &= common_bit_mask
#     return ones

# driver code
#
#
# print("The element with single occurrence is ",
#       getSingle(n, k))

# This code is contributed by "Abhishek Sharma 44"


# thefifthshop
# k, arr = int(input()), list(map(int, input().split()))
#
# myset = set(arr)
#
# # print(sum(arr))
# # print(sum(myset))
#
# print(myset)
# # print(arr*k)
# print(sum(myset)*k)
# print((sum(arr)))
# print(sum(myset)*k-sum(arr))
# print(((sum(myset)*k)-(sum(arr)))//(k-1))

from collections import Counter
_ = int(input())
print(Counter(map(int, input().split())).most_common()[-1][0])
