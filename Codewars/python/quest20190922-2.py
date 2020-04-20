# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
# print(sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# seq = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# for i in seq:
#     print(seq[i:len(seq)])
#
# print(seq[0:4])

#Best Practice
def maxSequence(arr):
    maxsum = curr = 0
    for x in arr:
        curr = curr + x
        if curr < 0: curr = 0
        if curr > maxsum: maxsum = curr
    return maxsum

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
