
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n > 1:
            sum_ = n + 1
            for i in range(2, n):
                if n%i==0:
                    sum_ = sum_ + i
            return sum_
        else: return 1

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

# def divisorSum(n):
#     divisors = []
#     i = 1
#     while n >= 1:
#         if (n%i==0):
#             print(i)
#             divisors.append(i)
#         i += 1
#     return sum(divisors)
#
# print(divisorSum(n))
