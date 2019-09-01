# https://www.hackerrank.com/challenges/bigger-is-greater/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    #basic algorithm:
    # 1. find when there is downfall found in the string, starting from the last. that is the 
         #point from where the right part of the string should be edited. Left part 
         #remains unupdated.
    
    # 2.The right part requires the first character to be exchanged by the next highest char
        #in the right part
    # 3. rest of the characters along with exchanged character in right are to be sorted.
    # 4. Then all of these are concatenated in this order.
    
    #eg. dkhc :: start from c to d . At d, we find the downfall from k to d. So, d will be our
    #right string. Here, there is no left string.
    #Now exchange d with next higher character ie. h.
    #so it becomes hkdc. Now sort kdc and concatenate with left string which is '' here and 'h'
    # so , ''+h+'cdk' ie. hcdk is the solution
    prevChar = w[len(w)-1]
    change = -1
    unchangedString = ""
    changedString = ""
    #check from last of the string till when the character downfall happens
    #eg. dkhc start from c , since c<h, continue, h<k, continue,k>d. split string
    #from here into unchanged and changed string. Unchanged string will not be changed.
    #eg. abcde d<e. So, unchanged string will be abc and changed will be de.
    for i,c in enumerate(reversed(w)):
        print(c)
        if c<prevChar:
            print(i," ",c," ",prevChar)
            change = len(w)-(i+1)
            unchangedString = w[0:change]
            changedString = w[change:len(w)]
            break;
        
        prevChar = c
        
    # if whole string traversed and downfall not found, return no answer
    if change == -1:
        return "no answer"
    print(change," ",unchangedString," ",changedString)
    
    #convert changed string to list as string is immutable.
    changedStringList = list(changedString)
    print(changedStringList)
    #sort the string so that the char next to the change can be found.
    #eg. dkhc, char larger than d is required which will be substituted for d
    #which is h.
    sortedChangedStringList = sorted(changedStringList)
    print(sortedChangedStringList)
    
    for i,c in enumerate(sortedChangedStringList):
        if c == w[change]:
            charGTSFE = sortedChangedStringList[i+1]
            charGTSFEi = i+1
    print("charGTSFE", charGTSFE, charGTSFEi)
    #charGTSFE is the character just greater than first char of changedString ie
    #in dkhc, h is charGTSFE which is greater than d
    
    #final string will be formed by concatenating the unchaned string, the character which
    #replaces the first char in changedString and the sorted list of remaining characters
    finalString = unchangedString+charGTSFE
    for i,c in enumerate(sortedChangedStringList):
        if i== charGTSFEi:
            continue
        finalString = finalString + c
    print("finalString is: ", finalString)
    return finalString
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()


