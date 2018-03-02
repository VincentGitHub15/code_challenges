#!/bin/python3

import os
import sys


#
# Complete the berthType function below.
#
def berthType(n):
    # Return the type of berth as described in the output format section.

    for i in range(7,73,8):
        if n == i:
            return 'SLB'

    for i in range(8,73,8):
        if n == i:
            return 'SUB'
        
    for i in range(1,73,8):
        if n == i or n == i -5:
            return 'LB'
            # print(i-5)
            # print(i)
    for i in range(2,73,8):
        if n == i or n == i -5:
            print(i-5)
            print(i)
            return 'MB'
    for i in range(3,73,8):
        if n == i or n == i -5:
            return 'UB'

        


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = berthType(n)

    f.write(result + '\n')

    f.close()