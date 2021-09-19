import numpy as np
np.set_printoptions(sign=' ')  # necessary do to old formatting in exp results
arr = np.array(input().split(), float)
print(np.floor(arr), np.ceil(arr), np.rint(arr), sep='\n')

# auch cool thx to GeoMatt22
print(*(f(arr) for f in [np.floor, np.ceil, np.rint]), sep='\n')
