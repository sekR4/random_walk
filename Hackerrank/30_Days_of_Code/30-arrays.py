# n = input()
# print(str(input())[::-1])


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    # my solution:
    # string = ''
    # for i in arr[::-1]:
    #     string += str(i)
    #     string += ' '
    #
    # print(string.rstrip())

    # best practice1:
    print(' '.join(map(str, reversed(arr))))

    # best practice2:
    print(*reversed(arr))
