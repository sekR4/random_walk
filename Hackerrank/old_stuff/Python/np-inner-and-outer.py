import numpy as np

A, B = np.array(input().split(), int), np.array(input().split(), int)
print(np.inner(A,B), np.outer(A,B), sep='\n')

# Also see:
# https://www.wikiwand.com/en/Inner_product_space
# https://www.wikiwand.com/en/Outer_product
