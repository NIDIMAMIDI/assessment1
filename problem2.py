"""
Question 2 - 
Description: 
        Write a program in Python to print the number of unique letters in a string.
        Only new letters from the string should be counted and not duplicates.

        Input : string1 = "India"
        Output : uniqueLetters = i,n,d,a

        Input : string1 = "Dedication"
        Output : uniqueLetters = d,e,i,c,a,t,o,n

"""

                #code

string = input("string1=")      # we can take input from user ......
name = string.lower()           # to convert the given string into a lower case
set = set(name)                 # converts string into set, set reomves duplicate elements in it 
list = []                       # defining a empty list to store the individual unique characters 
for character in name:
    if character in set:
        list.append(character)
        set.remove(character)
print("uniqueLetters=",(",".join(list)))

"""
            OUTPUT 
TESTCASE-1:

string1=Sharuk
uniqueLetters= s,h,a,r,u,k

TESTCASE-2:

string1=Museum
uniqueLetters= m,u,s,e
"""