import numpy as np

n,m = input().split()

N = int(n)
M = int(m)

arr=[]
for pair in range(N):
    arr.append(list(map(int, input().split())))

np_arr = np.array(arr)
print(np.min(np_arr, axis = 1).max())
