import numpy as np

n,m = input().split()

N = int(n)
M = int(m)

arr=[]
for pair in range(N):
    arr.append(list(map(int, input().split())))

np_arr = np.array(arr)

np.set_printoptions(legacy='1.13')
print(np.mean(np_arr, axis = 1))
print(np.var(np_arr, axis = 0))
print(round(np.std(np_arr),11))
