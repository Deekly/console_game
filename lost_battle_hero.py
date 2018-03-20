#
#                                #_Cubes
#
#   ny hz karoch, tyt beskonechnyj cykl // ( + ~40 min ) Yje net xD
#       UPD:    моя первая игра на Пайтоне, за которую, походу, не будет стыдно XD
#               Tuesday, 10.10.2017, 1:10am;

import random
import os

hello = """
                You're in trap!!! An army of trolls around you!
               But our Hero stays on the hill of dead enemies..."""

cube = """ 
           _________
        __/*********|_
       | /*********/  |
       | |*********|  |
       | \*********|  |
       |  |********|  |
       | /*********/  |
       | \_________\  |
       |______________|

        """
cube1 = """

        ______________
       |              |
       |              |
       |              |
       |       O      |
       |              |
       |              |
       |______________|

        """
cube2 = """

        ______________
       |              |
       |   O          |
       |              |
       |              |
       |              |
       |           O  |
       |______________|

        """
cube3 = """

        ______________
       |              |
       |  O           |
       |              |
       |       O      |
       |              |
       |           O  |
       |______________|

        """
cube4 = """

        ______________
       |              |
       |  O        O  |
       |              |
       |              |
       |              |
       |  O        O  |
       |______________|

        """
cube5 = """

        ______________
       |              |
       |  O        O  |
       |              |
       |       O      |
       |              |
       |  O        O  |
       |______________|

        """
cube6 = """

        ______________
       |              |
       |  O        O  |
       |              |
       |  O        O  |
       |              |
       |  O        O  |
       |______________|

        """

rand = random.randint(1,6)
cvar = 0
score = 0
print("\n\t\t\t Are you ready?!!")
print("""

            You're surrounded by enemies, many of which are already 
                          lying dead under your feet. 
        There are very few trolls left, but the strength is running out.
                  Collect 10 dice rolls 40 and over to win.

""")
input("\n\n\t\t\t!!!   Press ENTER to START   !!!")
os.system('cls')
print(hello)
print(cube)
print("\n\n\t Times: ", cvar)
print("\t Score: ", score)
input("\n\n\n\t\tPress ENTER to START")
os.system('cls')


while cvar < 9:
    if rand == 1:
        print(hello)
        print(cube1)
        cvar += 1
        score += rand
        print("\n\n\t Times: ", cvar)
        print("\t Score: ", score)
        input("\n\n\t\tPress Enter to continue, please =)")
        rand = random.randint(1,6)
        os.system('cls')
    if rand == 2:
        print(hello)
        print(cube2)
        cvar += 1
        score += rand
        print("\n\n\t Times: ", cvar)
        print("\t Score: ", score)
        input("\n\n\t\tPress Enter to continue, please =)")
        rand = random.randint(1,6)
        os.system('cls')
    if rand == 3:
        print(hello)
        print(cube3)
        cvar += 1
        score += rand
        print("\n\n\t Times: ", cvar)
        print("\t Score: ", score)
        input("\n\n\t\tPress Enter to continue, please =)")
        rand = random.randint(1,6)
        os.system('cls')
    if rand == 4:
        print(hello)
        print(cube4)
        cvar += 1
        score += rand
        print("\n\n\t Times: ", cvar)
        print("\t Score: ", score)
        input("\n\n\t\tPress Enter to continue, please =)")
        rand = random.randint(1,6)
        os.system('cls')
    if rand == 5:
        print(hello)
        print(cube5)
        cvar += 1
        score += rand
        print("\n\n\t Times: ", cvar)
        print("\t Score: ", score)
        input("\n\n\t\tPress Enter to continue, please =)")
        rand = random.randint(1,6)
        os.system('cls')
    if rand == 6:
        print(hello)
        print(cube6)
        cvar += 1
        score += rand
        print("\n\n\t Times: ", cvar)
        print("\t Score: ", score)
        input("\n\n\t\tPress Enter to continue, please =)")
        rand = random.randint(1,6)
        os.system('cls')

os.system('cls')

if score >= 40:
    print("""
    
                                 !!!!!!!!!!!!!!!!!!!!
                                 !!!   YOU WIN   !!!!
                                 !!!!!!!!!!!!!!!!!!!!
    
    """)
    print("\n\t\t Your Score: ", score)
    print("\t\t Your tries: ", cvar)
else:
    print("""
    
                                 !!!!!!!!!!!!!!!!!!!!
                                 !!!   YOU LOSE  !!!!
                                 !!!!!!!!!!!!!!!!!!!!
    
    """)
    print("\n\t\t Your Score: ", score)
    print("\t\t Your tries: ", cvar)


input("\n\n\t\tPress Enter to close app, please =)")
