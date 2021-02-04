#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalSwaps = 0
for i in range(n):
    numberOfSwaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            numberOfSwaps += 1
    
    totalSwaps += numberOfSwaps
    
    if numberOfSwaps == 0:
        break
    
print(f"Array is sorted in {totalSwaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[n-1]}")
