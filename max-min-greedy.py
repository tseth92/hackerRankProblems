'''https://www.hackerrank.com/challenges/angry-children/problem'''

####### Important : use sorted(arr) instead of ##################
#### arr.sort() as it is way much faster and helps solve all tc's
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    #print(arr)
    #print('printing arr')
    arr = sorted(arr)
    #print(arr)
    min_unfairness = 10000000000
    for i,v in enumerate(arr):
        #print('i ois: ', i,k)
        #print('i+1%k is: ',(i+1)%k)
        if i+1 >= k:
            curr_unfairness = arr[i]-arr[i-k+1]
            if curr_unfairness < min_unfairness:
                min_unfairness = curr_unfairness
    return min_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

