fruits = ["apple", "guava", "cherry", "banana"]

while 1:
    user = input("1) 把每個水果名稱改成大寫\n2）按照字母排序 a -> z\n3) 新增一種水果\n4）刪除一種水果\n5）還原成預設的水果清單\n請輸入選項(1-5)或按Q/q 結束：")

    if user == "1":
        fruits = [x.upper() for x in fruits]

    elif user == "2":
        fruits = sorted(fruits)

    elif user == "3":
        fruits.append("grapes")

    elif user == "4":
        fruits.remove(fruits[-1])   

    elif user == "5":
        fruits = ["apple", "guava", "cherry", "banana"]
    
    elif user == "q" or user == "Q":
        print("program ended!")
        exit()

    else:
        print("invalid input")

    print(fruits, "\n")