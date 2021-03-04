# There is a large pile of socks that must be paired by color. Given an array of integers 
# representing the color of each sock, determine how many pairs of socks with matching colors there are.
# Example

# There is one pair of color  and one of color . There are three odd socks left, one of each color. 
# The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs
# Input Format

# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.

def sockMerchant(n, ar):
    mySet = set() #hold all the values will see
    count = 0
  
  #everytime we a see a number we first check if it is already in the set
    #if it is  delete the number
    for i in range(n):
        if ar[i] in mySet:
            mySet.remove(ar[i])
            count+=1
        else:
            mySet.add(ar[i])

    return count
            
            
    #add one to the count
    #otherwise if we've never seen the number before add it to the set and continue
    
    
    #once we are done with the array 
    #return the count
  
  
  
n = 9
ar = [10,20 ,20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))
                