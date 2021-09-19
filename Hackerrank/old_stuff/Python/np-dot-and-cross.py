import numpy as np
n = int(input())
print(np.matmul(np.array([input().split() for _ in range(n)], int),
                np.array([input().split() for _ in range(n)], int)))

# A = np.array([input().split() for _ in range(n)], int)
# B = np.array([input().split() for _ in range(n)], int)

# print(np.matmul(A, B))
