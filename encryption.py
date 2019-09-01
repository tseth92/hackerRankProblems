# https://www.hackerrank.com/challenges/encryption/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    sLen = len(s)
    srow = math.floor(math.sqrt(sLen))
    scol = math.ceil(math.sqrt(sLen))
    if srow*scol < sLen:
        srow = srow+1
    #strMatrix = [[0 for i in range(scol)] for j in range(srow)]
    print(srow," ",scol)
    numWords = scol
    listWords = []
    for i in range(numWords):
        listWords.append('')
    print(listWords)
    curri = 0
    
    for i,char in enumerate(s):
        print("scol is:", scol,"i is : ",i," and char is: ", char," and scolmod is : ",scol%(i+1))
        print(curri)
        if curri>=scol:
            curri = 0
            listWords[curri] = listWords[curri]+char
            print("inIf")
        else:
            listWords[curri] = listWords[curri]+char
        curri = curri+1
        
    print(listWords)
        
    finalstr = ''
    for i in listWords:
        print(i)
        finalstr = finalstr+i+' '
    print(finalstr)
    return finalstr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

