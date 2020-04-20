#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# my solution
# Complete the factorial function below.
def factorial(n):
    if n <= 1: return 1
    else: return n * factorial(n - 1)

print(factorial(int(input())))

# best practice
# factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
# print(factorial(int(input())))
