# repeated string
#hackerrank Challenge #4
# There is a string s, of lowercase letters that is repeated infinetly manytimes. Given an integer n n, findnd print the number 
#of letter a's in the first nletters of the infinite string

# so example  1
#abcac
#10

#abcacabca this string appears an infinte amount of times, but since we are only considering the first ten letters
#in those first ten letters we we count only 4 times that a appears

#ex 2 
#aba
#10
#only considering the first 10 letters aba,aba,aba,a
#and we count only 7 a's

#ex 3 
# a
# 10000000

#since a is the only letter and we are considering 10000000, return 10000000

def repeatedString(s,n):
    #base case if a is the only letter in the group, return n
        #all function 
        checkMe = all(x == s[0] for x in s)
        if checkMe:
            return n
        else:
            myMap = {}
            # can iterate through the stirng up to n, since its infinte
            for char in range(n):
            # at each letter we see, count the frequency of the letter 
                  #add it to the overall count (value) of the dictionary 
                if (s[char] in myMap):
                    myMap[s[char]] +=1
                #otherwise add it the map as a new character and give it a freq of 1
                else:
                    myMap[s[char]] = 1
            #finally return the value of a as our answer
            return myMap['a']
        
myS = "abaabaabaa"
n = 10
print(repeatedString(myS,n))
