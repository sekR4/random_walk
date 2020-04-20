#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
cnt=0
for i in range(len(a)-1):
    for j in range(len(a)-1 - i):
        if a[j] > a[j+1]:
            cnt += 1
            a[j], a[j+1] = a[j+1], a[j]

print('Array is sorted in {} swaps.'.format(cnt))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[len(a)-1]))
