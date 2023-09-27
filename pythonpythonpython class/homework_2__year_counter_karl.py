'''

This is a program for checking leap year

made by karl_hsiao

'''

def if_leap(year):
    #A function for checking leap year
    if year % 400 == 0:
        #leap year is a year that can be divisable by 400 or 4 and not 100 thus checking the mod of 400 and 100 and 4 can separate leap and norm year
        return "西元" + str(year) + "年為潤年"
    
    elif year % 100 == 0:

        return "西元" + str(year) + "年為平年"
    
    elif year % 4 == 0:

        return "西元" + str(year) + "年為潤年"

    else:
        return "西元" + str(year) + "年為平年"
        #returning results

if __name__ == "__main__":
    for i in range(5):
        #run 5 times
        print("Test case",i)
        #print the # of case

        year = int(input("請輸入西元年："))
        #inputs

        print(if_leap(year))
        #print result

