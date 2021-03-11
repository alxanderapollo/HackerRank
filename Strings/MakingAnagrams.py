# A student is taking a cryptography class and has found anagrams to be very useful. 
# Two strings are anagrams of each other if the first string's 
# letters can be rearranged to form the second string. In other words, both strings 
# must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, 
# but bacdc and dcbad are not.

# The student decides on an encryption scheme that involves two large strings. 
# The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. 
# Determine this number.

# Given two strings, a and  b, that may or may not be of the same length, determine the minimum number of character deletions required 
# to make a and b anagrams. Any characters can be deleted from either of the strings.

#example from hackrank
#a ='cde'
#b = 'dcf
#number of deltions to make this an anagram 4 


#my own examples 
#if they are the same lenght
#alex -> sorted -> aelx
#xale -> sorted aelx 

#if one is bigger in length the other
#a = marblzeasal -> sorted  -> aaabellmrsz
#b = marbl -> sorted -> ablmr

# Working algorithm 
#1.store both strings into a hashmap, counting the frequency of each char in each respective string
#2.using the string with the smallest length compare the frequency of chars in the smaller with the larger string
#3.each time we find a char add it to count varaible +=1, 
#4. the second we find that there are no more matching chars in the longest string, 
#5 take the count varaible subtract and subtract it from the length of the larger string, that will be the diffrence of how many chars needs to be cut and our return answer

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    pass
