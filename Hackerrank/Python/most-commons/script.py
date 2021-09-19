# s, d = input(), {}
# char_set = sorted(set(s))
# for char in char_set:
#     d[char] = s.count(char)

# d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# for idx, i in enumerate(d):
#     if idx < 3:
#         print(i, d[i])

# Wow... Nice solution from Boki
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
