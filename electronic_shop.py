# https://www.hackerrank.com/challenges/electronics-shop/problem
#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    maxVal = -1
    keyboards.sort(reverse=True)
    drives.sort()
    print(keyboards)
    print(drives)
    for i,valKey in enumerate(keyboards):
        for j,valDrive in enumerate(drives):
            print('i is :',i,"j is: ",j)
            if keyboards[i]+drives[j] > b:
                break
            if keyboards[i]+drives[j] > maxVal :
                maxVal = keyboards[i]+drives[j]
    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

