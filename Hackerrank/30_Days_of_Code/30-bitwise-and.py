#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        # s = list(range(1,n+1))
        # if n!=k: print(max([i if i<k else 0 for i in s]))
        # else: print(0)
        print(k-1 if ((k-1) | k) <= n else k-2) #tribute goes to jekus
