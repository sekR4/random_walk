import numpy as np
n, m, _ = map(int, input().split())
print(np.array([list(map(int, input().split())) for _ in range(n+m)]))
