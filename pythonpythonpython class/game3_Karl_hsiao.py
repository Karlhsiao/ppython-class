"""

This is a game of guessing number with hiding number

"""

import random
#imports


if __name__ == "__main__":
    while True:
        ans = random.randint(1000, 10000)
        win = 0
        big_ret = "****"
        counter = 1
        #presettings

        while True:

            while True:
                guess = input("guess a 4 digit num: ")
                ret = "" #inputs valid checking and checking

                try:
                    if len(guess) != 4:
                        print("The length of the number is not correct.")
                        continue 
                        #check length of input
                        

                    else:
                        int(guess)
                        #check if its a integer
                        break

                except:
                    print("invalid input!")
                    #print error message
            

            for i in range(4):
                if int(guess) == ans:
                    print("The answser is " + str(ans) + "!")
                    win = 1
                    break
                    #win result

                elif str(guess)[i] == str(ans)[i]:
                    ret += guess[i]

                else:
                    ret += "*"
                #calculate hint message

            if win == 1:
                break
            #check win

            counter += 1

            print("guessed times:", counter, "your hint:", ret, "\n")
            #hint message

        again = input("you win! press 'y' or 'Y' to play again, press other keys to end: ")
        #play again

        if again == "y" or again == "Y":
            continue

        else:
            break
        #quit game

                