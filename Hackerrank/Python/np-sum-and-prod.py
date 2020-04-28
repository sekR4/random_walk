import numpy as np

n, _ = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.prod(np.sum(arr, axis=0), axis=0))
