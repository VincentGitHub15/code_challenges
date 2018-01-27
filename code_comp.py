#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    best = 0
    for a0 in range(n):
        name, d, j = input().strip().split(' ')
        name, d, j = [str(name), int(d), int(j)]
    # Write Your Code Here
        #print(a0, name, d, j)
        max_diff = j - d
        if max_diff > best:
            best = max_diff
            coder = name
            appearance = a0
        elif max_diff == best:
            best = max_diff
            if a0 < appearance:
                coder = name
    print(coder, best)