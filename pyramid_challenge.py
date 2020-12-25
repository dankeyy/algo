#!/usr/bin/env python3

print(1)
n = 2

for row in range(15):
    for i in range(row + 2): # +2 cause we start from second row and "row" starts from 0
        print(n + i, end = ' ')

    n = 2*n + 1
    print()

"""
should come out as such (depends on how many rows you want it to print)
1
2 3 
5 6 7 
11 12 13 14 
23 24 25 26 27 
47 48 49 50 51 52
"""