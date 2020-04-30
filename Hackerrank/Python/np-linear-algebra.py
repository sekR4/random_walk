import numpy as np

# print(np.linalg.det([[1.1, 1.1], [1.1, 1.1]]))
#[[1.1, 1.1], [1.1, 1.1]]
# a=[list(map(float,input().split())) for _ in range(int(input()))]
print(round(np.linalg.det([list(map(float,input().split())) for _ in range(int(input()))]),2))

#testcase
# print(round(np.linalg.det([[1.1, 1.1],[1.1, 1.2]]),2))
