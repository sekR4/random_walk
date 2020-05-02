import os
import collections
# s = 'AABCAAADA'
# k = 3
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # set working directory
with open('merge-the-tools-test-case-1-input.txt', 'r') as file:
    inp = file.read()
    s, k = inp.split('\n')[0], int(inp.split('\n')[1])


# tmp, len_tmp = [], 0

# for i in s:
#     len_tmp += 1
#     if i not in tmp:
#         tmp.append(i)
#     if len_tmp == k:
#         print(''.join(tmp))
#         tmp, len_tmp = [], 0

# tmp, len_tmp = '', 0
# for letter in s:
#     len_tmp += 1
#     if letter not in tmp:
#         tmp += letter
#     if len_tmp == k:
#         print(tmp)
#         tmp, len_tmp = '', 0


# tmp = ''
# # print(len(tmp))
# for letter in s:
#     if letter not in tmp:
#         tmp += letter
#     if len(tmp)-1 == k:
#         print(tmp)
#         tmp = ''
# inspired by lesingerouge
def merge_the_tools(string, k):
    tmp, len_tmp = '', 0
    for letter in string:
        len_tmp += 1
        if letter not in tmp:
            tmp += letter
        if len_tmp == k:
            print(tmp)
            tmp, len_tmp = '', 0


#
#
merge_the_tools(s, k)
