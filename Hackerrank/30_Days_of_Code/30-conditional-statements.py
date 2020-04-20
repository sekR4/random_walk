#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    # If N is odd, print Weird
    if N%2 != 0: print('Weird')
    # If N is even and in the inclusive range of 2 to 5, print Not Weird
    if N%2 == 0 and N>=2 and N<=5: print('Not Weird')
    #If N is even and in the inclusive range of 6 to 20, print Weird
    if N%2 == 0 and N>=6 and N<=20: print('Weird')
    #If N is even and greater than 20, print Not Weird
    if N%2 == 0 and N>20: print('Not Weird')
