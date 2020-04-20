# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
# test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")

# def stock_list(listOfArt, listOfCat):
#     ....

# import re
# import pandas as pd

# t="RA 200"
# p1,p2 = re.compile('^.'),re.compile('\d+')
# print(p1.findall(t),p2.findall(t))

# key = []
# val = []
# for i in b:
#     if p1.findall(i)[0] in c:
#         #geht vermutl nicht wegen best. object type? ja, liste
#         print(p1.findall(i)[0],p2.findall(i)[0])
        # key.append(p1.findall(i)[0])
        # val.append(p2.findall(i)[0])


# res = []
# for group in c:
#     amount = []
#     for i in b:
#         if p1.findall(i)[0] in group:
#             amount.append(int(p2.findall(i)[0]))
#     # print(group,sum(amount))
#     res.append('({} : {})'.format(group,sum(amount)))
#
# # print(res)
# print(' - '.join(res))
import re

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

def stock_list(listOfArt, listOfCat):
    p1,p2 = re.compile('^.'),re.compile('\d+')
    result = []
    for cat in listOfCat:
        amount = [int(p2.findall(i)[0]) for i in listOfArt if p1.findall(i)[0] in cat]
        result.append('({} : {})'.format(cat,sum(amount)))
    return ' - '.join(result) if len(listOfArt) > 0 else ''

stock_list(b,c)
#
# print(key)
# print(val)

# df = pd.DataFrame(val,key)

# print(df.head())
# print(df.keys)
#
# help(pd.groupby())

        # for group in c:
        #     print(group)


# for group in c:
#     for i in b:
#         if p1.findall(i)[0] in c:
#             #geht vermutl nicht wegen best. object type? ja, liste
#             print(p1.findall(i),p2.findall(i))




# l1 = ['A', 'B', 'C']
# l2 = ['A', 'B']
#
# for i in l1:
#     if i in l2:
#         print(i)


# for i in b:
#     print(i.match('^A'))
