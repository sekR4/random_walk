# my solution (works)
from collections import OrderedDict
import re

N, d = int(input()), OrderedDict()

for i in range(N):
    s = input()
    item_name, net_price = re.findall('\D+', s)[0].rstrip(), int(re.findall('\d+', s)[0])
    if item_name not in d: d[item_name] = net_price
    else: d[item_name] = d[item_name] + net_price

for i in d:
    print(i, d[i])

# best practice?
from collections import OrderedDict
d = OrderedDict()

for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)

for item, quantity in d.items():
    print(item, quantity)
