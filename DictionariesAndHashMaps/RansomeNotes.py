# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his 
# handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to 
# create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use 
# only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.
# Given the words in the magazine and the words in the ransom note, print Yes if he can 
# replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
# For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". 
# The magazine has all the right words, but there's a case mismatch. The answer is NO

#examples
#input
# give me one grand today night
# give one grand today

# output - yes, have all the words and right number of frequency 

#input
# two times three is not four
# two times two is four

# output - no missing two, twos
# ive got a lovely bunch of coconuts
# ive got some coconuts

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    #base case the length of the  string from the mag, is  smaller than the length of the written note - return no 
    if len(magazine) < len(note):
        return "No"
    else:
        #algorithm 
        #store both strings in their own containers
         #as we store strings count the frequency of each word and add that as the val
        myMag = magazine.split(' '); myNote = note.split(' ')
        holdMyMag = {}; holdMyNote= {} 
        #magazine
        # if its in the map already, add one to the freq
        for i in range(len(myMag)):
            if myMag[i] in holdMyMag:
                holdMyMag[myMag[i]] +=1
        #otherwise create a new key - val
            else:
                holdMyMag[myMag[i]] = 1
            
        #killers note
        for i in range(len(myNote)):
            if myNote[i] in holdMyNote:
                holdMyNote[myNote[i]] +=1
        #otherwise create a new key - val
            else:
                holdMyNote[myNote[i]] = 1
            
        #once we're done look at the contianer that has the note, compare the value (freq) of the said string and if there is match continue
        
        #check Frequency
        print(holdMyMag)
        print(holdMyNote)
        # we want to only look at the strings that are the same as note container anything else doesnt matter
        for key, val in holdMyNote.iteritems():
            if key in holdMyMag and val == holdMyMag[key]:
                continue
            else:
                return "No"
        return "Yes"
     
        
        #if we succesffully get through both containers with matching frequncy of words then its yes
        #otherwise the second we come across a missing word or mis match of freq send no

myMag = 'two times three is not four'
myNote = 'two times two is four'
print (checkMagazine(myMag,myNote))

