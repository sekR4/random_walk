N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))


# N = 5
# X = [10, 40, 30, 50, 20]
# W = [1, 2, 3, 4, 5]


print(round(sum([X[i]*W[i] for i in range(len(X))])/sum(W),1))
