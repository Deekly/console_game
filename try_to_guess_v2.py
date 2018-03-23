#   try_to_guess
#   coded by Deekly
#   21.03.18

#   Try to guess my number from 1 to 100

import random

print ("""
                            !!! TRY TO GUESS !!!
                            
                        blah blah blah blah blah blah
                        blah blah blah blah blah blah
                        blah blah blah blah .... ....
""")

input ("\t\t\tPress enter if understood")

rand = random.randint(1,100)

print ("Lets start =)")

count = 1
digit = 0
print ("Enter Sandman:")    
while digit != rand:
    digit = int(input())
    if digit > rand:
        print ("Try less")
        count += 1
    else:
        print ("Try more")
        count += 1
    

print ("\t\t\t !!! YOU WIN !!!")
print ("Your result:", count)

input()
