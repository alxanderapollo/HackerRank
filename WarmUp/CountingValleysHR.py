#!/bin/python3

import math
import os
import random
import re
import sys

# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  
# step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Example
# The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.

# Function Description

# Complete the countingValleys function in the editor below.

# countingValleys has the following parameter(s):

# int steps: the number of steps on the hike
# string path: a string describing the path
# Returns

# int: the number of valleys traversed
# Input Format

# The first line contains an integer , the number of steps in the hike.
# The second line contains a single string , of  characters that describe the path.
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