import numpy as np

_ = map(int, input().split())

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print('[' + str(A+B) + ']')
print('[' + str(A-B) + ']')
print('[' + str(A*B) + ']')
print('[' + str(A//B) + ']')
print('[' + str(A % B) + ']')
print('[' + str(A**B) + ']')
