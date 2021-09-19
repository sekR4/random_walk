#https://numpy.org/doc/stable/reference/generated/numpy.polyval.html?highlight=polyval
import numpy as np
print(np.polyval(list(map(float,input().split())),float(input())))

# my solution worked, but H_Shen's looks also interesting:
print(__import__('numpy').polyval(list(map(float,input().split())),float(input())))
