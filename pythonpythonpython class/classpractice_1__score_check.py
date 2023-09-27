'''
This is a grade checking script

by Karl_hsiao
'''


for i in range(5):
    print("Test case " + str(i+1) + "：")

    cl = input("請輸入科目：")
    grade = input("請輸入分數：")

    #inputs here

    #check diff type of class here
    if cl == "國文":

        if int(grade) >= 70:
        #check grades here
            print("恭喜及格！")
        else:
            print("加油！差點就及格了！")

    #check english class here
    elif cl == "英文":

        if int(grade) >= 60:
            print("恭喜及格！")
        else:
            print("加油！差點就及格了！")

    #invalid class
    else:
        print("沒有考這科喔")