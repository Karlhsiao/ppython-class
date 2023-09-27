'''

This is a program for 2 problem solving select by 1 or 2

made by karl_hsiao

'''


game = input("選擇 1)溫度轉換 2)分蘋果問題：")
#inputs

if game == "1":
    #if game 1 chosed

    f = int(input("請輸入華氏溫度："))

    c = (f-32)*(5/9)
    #calc c number

    print("華氏" + str(f) + "度=攝氏" + str(c) + "度。")
    #print out


elif game == "2":
    #if game 2 chosed

    apple = int(input("蘋果數量："))
    kids = int(input("小朋友數量："))

    print("每人可分得" + str(apple // kids) + "顆蘋果，剩下" + str(apple % kids) + "顆蘋果。")
    #calc and print out

else:
    print("沒有這個選擇喔。")
    #else print