
##########################################
"""
Practice 1:
改寫程式讓輸出如下：
**********
**********
**********
"""

print("<Practice 1>")
i = 1
while i <= 3:
    print('**********')
    i += 1

##########################################
"""
Practice 2：
改寫程式讓輸出如下：
2 4 6 8
"""
print("\n<Practice 2>")

i = 2
while i <= 8:
    print(i, end = ' ')
    i += 2

##########################################
print("\n\n<Practice 3>")
"""
Practice 3：
使用 while + flag 的寫法改寫：
輸出：
1 3 5 7 9
"""

i = 1
finish = False
while not finish:
    print(i, end = ' ')
    i += 2
    if ( i > 10 ):
         finish = True


##########################################
print("\n\n<Practice 4>")
"""
Practice 4：
使用 while True + break 的寫法改寫：
輸出：
2 4 8 16 32 64
"""


i = 2
while True:
    print(i, end = ' ')
    i = i * 2
    if ( i > 65 ):
         break
     
##########################################
print("\n\n<Practice 5>")
"""
Practice 5：
寫一段程式讓使用者一直輸入整數N，直到輸入Q結束為止。

輸出：
請輸入一整數或Q/q結束：50
50 為偶數
請輸入一整數或Q/q結束：13
13為奇數
請輸入一整數或Q/q結束：0
0為偶數
請輸入一整數或Q/q結束：Q
Thank you, bye!
"""
while True:

    try:
        num = input("請輸入一整數或Q/q結束")
        
        if num == "q" or num == "Q":
            print("Thank you, bye!")
            break
        if int(num) % 2 == 0:
            print(f"{num}為偶數")
        else:
            print(f"{num}為奇數")

    except:
        print("輸入錯誤！請重新輸入")