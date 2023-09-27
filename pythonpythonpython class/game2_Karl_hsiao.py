"""

This is a computer guess guess the number game

by Karl_hsiao

"""

import random
#import

print("Rule: Think of 1-100 number and tell computer its upper or lower or bingo in result, computer will guess you number\n")

while True:
    bottom = 0
    top = 100
    counter = 0
    #setting up game

    while True:
        guess = random.randint(bottom, top)
        #computer guess

        print("computer:", guess)

        human = input("Is it upper/lower or bingo: ")
        #human reply

        if human == "upper":
            bottom = guess 

        elif human == "lower":
            top = guess - 1

        elif human == "bingo":
            again = input("GG! Computer took " + str(counter) + " times to get it! If you want to play again press y or Y: ")

            if again == "y" or again == "Y":
                play = 1
                break
        #reset up guess 

        counter += 1
        #counter