#   word_jumble
#   coded by Deekly
#   23.03.18

import random

WORDS = ("random","python","programming","code","imagination","hello world")

word = random.choice(WORDS)

correct = word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

print("""
                         !!! HELLO IN \"WORD JUMBLE\" !!!

            blah blah blah blah blah blah blah blah blah blah blah blah
            blah blah blah blah blah blah blah blah blah blah blah blah
            blah blah blah blah blah blah blah blah blah blah blah blah
            blah blah blah blah blah blah blah blah .... .... .... ....
""")

print("Jumbled word is:", jumble)

guess = input("\nTry to win!!!\n")

while guess != correct and guess != "":
    print("You're wrong...")
    guess = input("Try to win!!!\n")

if guess == correct:
    print("GOOD JOB!!!")
else:
    print("You're cheater!!!")

input("\n\nPress ENTER to quit")
