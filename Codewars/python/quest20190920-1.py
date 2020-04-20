# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH"
# are not directly opposite but they become directly opposite after the reduction
# of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# test.assert_equals(dirReduc(a), ['WEST'])
# u=["NORTH", "WEST", "SOUTH", "EAST"]
# test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

# def dirReduc(arr):

# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
a=["NORTH", "WEST", "SOUTH", "EAST"]
# print(set(a))





# for i in list(set(a)):
#     print(zip(i,a.count(i)))

# directs = {i: a.count(i) for i in a}
# print(directs)

# ns=["NORTH", "SOUTH"]
# ew=["EAST", "WEST"]

# ns = {"NORTH":1, "SOUTH":-1}
# ew = {"EAST":1, "WEST":-1}

# for k in ns:
#     print(k,directs.get(k))

# for k in directs:
#     print(k,directs.get(k)*ns.get(k,0))
#
# for k in directs:
#     print(k,directs.get(k)*ew.get(k,0))


# for k in directs:
#     print('ns',sum([directs.get(k)*ns.get(k,0)]))
# for k in directs:
#     print(k,directs.get(k)*ew.get(k,0))
# ns = sum([directs.get(k)*ns.get(k,0) for k in directs])
# print(ns)
#
#
# ew = sum([directs.get(k)*ew.get(k,0) for k in directs])
# print(ew)



# for k in ew:
#     print(k,directs.get(k))
