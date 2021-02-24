#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    #ideas when we go up we are going postive, 
    #when we go down we are going negative so count u as pos
    #D as negative 
    myValleyCount = 0
    myProgress = 0
    #need to write a way to check if we are going down first, because thats when we are counting
    for elem in path :
        
        if  elem == 'U': # go up
            if myProgress == -1: #if we are -1 away from reaching 0 then we have traversed a valley since we will be back at zero
                myValleyCount+=1
            myProgress+=1
        if  elem == 'D': # go down 
             myProgress-=1
    
    return myValleyCount


myArray = [U,D,D,D,U,D,U,U]
mySteps = 8
print(countingValleys(mySteps,myArray))