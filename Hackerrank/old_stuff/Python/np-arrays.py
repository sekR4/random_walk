import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    np_arr = numpy.array(arr,dtype=float)
    return np_arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# print(arr)
