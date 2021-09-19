#!/bin/python3

import math
import os
import random
import re
import sys

# IDs = []
names = []

if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if emailID[-10:] == '@gmail.com': names.append(firstName)

for name in sorted(names): print(name)


# email = 'riya@gmail.com'
# print(email[-10:])
