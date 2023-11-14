order = {"order_number" : "001",
         "product" : "蘋果", 
         "price" : 50, 
         "quantity" : 3, 
         "total_price" : 150} 

def change_order_num(order, num):
    order["order_number"] = num
    print("訂單號碼修改為", num)

    return order

def change_product(order, name):
    order["product"] = name
    print("訂單品名修改為", name)

    return order

def change_price(order, price):
    order["price"] = price
    print("訂單單價修改為", price)

    return order

def change_quantity(order, quant):
    order["quantity"] = quant
    print("訂單數量修改為", quant)

    return order

def check_price(order):
    order["total_price"] = order["quantity"] * order["price"]
    print(order["total_price"])

if __name__ == "__main__":
    print("預設訂單: ", order)
    while True:
        chose = input("功能選項： 1)修改訂單號碼 2)修改品名 3)修改單價 4)修改數量 5)查詢訂單金額 6)印出訂單: ")

        if chose == "1":
            num = input("請輸入訂單號碼: ")
            order = change_order_num(order, num)
        
        elif chose == "2":
            name = input("請輸入品名: ")
            order = change_product(order, name)

        elif chose == "3":
            price = int(input("請輸入價格: "))
            order = change_price(order, price)

        elif chose == "4":
            quantity = int(input("請輸入數量: "))
            order = change_quantity(order, quantity)

        elif chose == "5":
            print("查詢訂單金額")
            check_price(order)

        elif chose == "6":
            print("印出訂單")
            print(order)

        else:
            break
