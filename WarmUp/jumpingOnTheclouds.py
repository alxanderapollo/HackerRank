# Complete the jumpingOnClouds function below.
# an array of 0's and 1's 0 is safe to jump on, and 1 must be jumped over 
#the problem asks that we determine the min number of jumps to reach the end of the array,
# c = [0,1,0,0,0,1,0] in this case index 1 and 5 must be avoided

# the ones are never consective, but the 0's are 

#algorithm 
    #initlize counting varibles and iterators
    #we jump by twos because its usally consecive zeroes
    #first check is to see if are at the end or one away from the end
    # if we are increment myyCount by one and move the iterator by one forward
    # otherwise keep jumping by 2's and adding 1 to the overall count
    #return the count

def jumpingOnClouds(c,skip = 1):
    #two things to look out for 
        myCount = 0
        i = 0
        length = len(c)
        
        
        while i < length-1:
            # if we are 2 away from the end incrment the iterator by 1
            #add 1 to the count, we move at once because we want to stop
            # before the one add a count and then properly jump over it
            if i+2 == length or c[i+2] == 1:
                i+=1
                myCount +=1
            #otherwise keep jumping by twos and incrementing by 1
            else:
                i+=2
                myCount+=1
        return myCount
                
myList = [0,0,0,0,1,0]
print( jumpingOnClouds(myList))


import sys
for line in sys.stdin:
    myint = type(int(line)) * type(int(line)) 
    print(line)
    print(myint)

 