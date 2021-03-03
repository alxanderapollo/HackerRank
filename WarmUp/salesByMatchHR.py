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
                