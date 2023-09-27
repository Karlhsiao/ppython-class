"""

This is a script about guessing a number between MIN and MAX

by Karl_Hsiao

"""

from random import randint
#import randint

MIN = 1
MAX = 100
q = 0
#rng range const
target = randint(MIN,MAX+1)
#take rng




while True:


    ans = input("請猜一個1～100的整數，或輸入Q/q離開：")
    #usr input

    if ans == "Q" or ans == "q":
        q = 1
    #if user input q then q
        
    if q == 1:
        break
    #qting

    while True:
        try:
            #check validality of input
            if ans == "Q" or ans == "q":
                q = 1

            if int(ans) == target:
                ans = input("BINGO! 輸入Y/y繼續玩,輸入其他字離開：")
                #usr input after win

                if ans == "Y" or ans == "y":
                    target = randint(MIN,MAX+1)
                    #retake rng
                    break
                #usr input y then keep playing

                else:
                    q = 1
                    break

            elif int(ans) < target:
                ans = input("猜大一點! 或輸入Q/q離開：")
                #usr input after getting bigger
                if ans == "q" or ans == "Q":
                    q = 1

            elif int(ans) > target:
                ans = input("猜小一點! 或輸入Q/q離開：")
                #usr input after getting lower
                if ans == "q" or ans == "Q":
                    q = 1

            if q == 1:
                break
            
        except:
            print("輸入錯誤！請重新輸入")
            #invalid input
            break
    
    if q == 1:
        break
    #end program
        

    


