# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.

def countSorted(tempList):
    ##print("tempList: ", tempList)
    arr = [0]*201
    arrFinal = [0]*(len(tempList))
    ##print("before count: ",arr)

    for i,val in enumerate(tempList):
    ## print("i is: ",val)
        arr[val] = arr[val]+1
    ##print("after count: ",arr)

    for i,val in enumerate(arr):
        if i==0:
            continue
        arr[i] = arr[i-1]+arr[i]
    ##print("after total count: ",arr)

    #print(arrFinal)
    for i,val in enumerate(tempList):
        ##print(arr[val])
        arrFinal[arr[val]-1] = val
        arr[val] = arr[val]-1
    ##print("arrFinal",arrFinal)
    return arrFinal

def activityNotifications(expenditure, d):
    #print(expenditure)
    tempList = []
    notification = 0
    print(d)
    ct =-1
    for i, exp in enumerate(expenditure):
        tempList.append(exp) 
        ##print("tempList before sorting: ",i, " : ",tempList)
        if i == d-1:
            ##print("i==d",tempList[i])
            tempList = countSorted(tempList)
        if i > d-1:
            #print('algo starts here',i)
            #if exp > tempList[i-1]:
            tempList = countSorted(tempList)
            ##print("tempList is: ",tempList)
            if i%2 != 0: #case of odd as rest of digits already present are odd:
                median = tempList[math.floor(i/2)]
                ##print("If tempList is: ",tempList," median is: ",median)
            else:
                median = 0.5*(tempList[math.floor(i/2)] + tempList[math.ceil(i/2)])
                ##print("Else tempList is: ",tempList," median is: ", median)
            if exp >= 2*median:
                notification = notification + 1
                print("sending notification: ", notification)
            ct = i
    print("Total notifications sent are : ",ct, notification)
    return notification


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)


    #fptr.write(str(result) + '\n')

    #fptr.close()

