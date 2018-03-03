import os
import sys


def minimumTotalUnhappiness(k, x):
    # Print the minimum sum of unhappiness across all houses.

    total = 0
    old_sum = 1000000
    for i in range(max(x)+1):
        # print('i', i)
        for j in range(k):
            # print('i,j', i, j)
            # print((i-j)**2)
            new_sum = ((i-j)**2)
            print('new,old', new_sum, old_sum)
            if new_sum < old_sum:
                print('newsum is less', new_sum)
                total += new_sum
            else:
                print('oldsum is less', old_sum)
                total += old_sum
            old_sum = new_sum
            # print('i,j','sum', i, j, sum)
            # total += sum
            # print('total:', total)
    print('final total:', total)


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    minimumTotalUnhappiness(k, x)