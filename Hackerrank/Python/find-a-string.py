def count_substring(string, sub_string):
    return sum([ 1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string])

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

string = 'ABCDCDCD'
sub_string = 'CD'
print(count_substring(string, sub_string))

# print(string.find(sub_string))
cnt = 0
occ_idx = 0
for i in range(len(string)-len(sub_string)+1):
    print(i,string[i:i+len(sub_string)])
    if string[i:i+len(sub_string)]==sub_string: print(1)
    # idx = string[i:].find(sub_string)
    # string = string[idx+1:]
    # print(string)
    # print(string[i], string[i:], string[i:].find(sub_string), string[string[i:].find(sub_string):])
    # occ_idx = occ_idx + 1
    # occ_idx = string[occ_idx:].find(sub_string)
    # if string[occ_idx:].find(sub_string) >= 0:
    #     cnt = cnt + 1

# print(cnt)
# print(string[occ])
# print(string[occ+1:])

# for i in range(len(string)):

# string, substring = (input().strip(), input().strip())
# print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
