import collections
s = 'AABCAAADA'
k = 3

t_length = len(s)//k

# print(t_length)
for i in range(k):
    # print(i)
    # print(s[i*t_length:t_length+i*t_length])
    # print(set(s[i*t_length:t_length+i*t_length]))
    print(''.join(collections.OrderedDict.fromkeys(s[i*t_length:t_length+i*t_length]).keys()))
# print(s[3])


def merge_the_tools(string, k):
    t_length = len(string)//k
    for i in range(k):
        print(''.join(collections.OrderedDict.fromkeys(
            string[i*t_length:t_length+i*t_length]).keys()))


merge_the_tools(s, k)
