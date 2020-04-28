import numpy as np
np.set_printoptions(legacy='1.13')  # hackerrank demands a certain format
n, _ = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.mean(arr, axis=1), np.var(arr, axis=0), round(np.std(arr), 12), sep='\n')
