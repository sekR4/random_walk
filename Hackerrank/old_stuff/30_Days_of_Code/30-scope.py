class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
    	      self.maximumDifference=max(a)-min(a)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# # Testing
# def maxdiff(arr):
#     diff = []
#     for i in arr:
#         for j in arr:
#             diff.append(abs(i - j))
#     return max(diff)
#
#
# print(maxdiff(a))