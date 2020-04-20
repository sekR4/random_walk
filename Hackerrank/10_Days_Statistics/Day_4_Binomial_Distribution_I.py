# from scipy.stats import binom
#
# x = list(map(float, input().split()))
#
# p = x[0]/sum(x)
# print(p)
# # print(binom.rvs(size=0,n=6,p=p))
# # print(binom(n=2,p=p).pmf())
# rv = binom(n=6, p=p)
# print(rv.pmf(4))

# import math
#
# def bi_dist(x, n, p):
#     b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
#     return(b)
#
# b, p, n = 0, 1.09/2.09, 6
# for i in range(3,7):
#     b += bi_dist(i, n, p)
# print("%.3f" %b)

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1 - p, n - k)


b, g = map(float, input().strip().split(' '))

result = round(sum([binomial(6, i, b / (b+ g)) for i in range(3, 7)]), 3)
print(result)
