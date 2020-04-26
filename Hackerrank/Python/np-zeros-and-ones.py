import numpy as np
dims = tuple(map(int, input().split()))
print(np.zeros(dims, int), np.ones(dims, int), sep='\n')
