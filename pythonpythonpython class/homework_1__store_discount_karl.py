'''

This is a program for store discount giving money that counts it

made by karl_hsiao

'''

if __name__ == "__main__":
    for i in range(5):
        print("Test case " + str(i+1) + "：")
        #print case

        cost = int(input("消費金額："))

        #inputs here

        #first phase question

        recharge5000 = (cost // 5000)
        #calc how much recharge from 5000

        cost1000 = cost - recharge5000*5000

        recharge1000 = (cost1000 // 1000)
        #calc how much recharge from 1000

        print("回饋金：" + str(recharge5000*600 + recharge1000*100))
        #add up both number

        #second phase question

        paymore = 1000 - (cost1000 % 1000)
        #calc how much you need to pay


        if cost1000>4000:
            #check how much you can get after
            morecharge = 200

        else:
            morecharge = 100

        print("再消費" + str(paymore) + "可多得回饋金"+ str(morecharge) + "喔！")
        #print out result
        

