import numpy as np
N, _ = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.transpose(arr), arr.flatten(), sep='\n')
