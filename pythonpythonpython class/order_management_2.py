order = {}

def create_product_order():
    products = {}
    while True:
        name = input()

        if name == "quit":
            return products
        
        price = input()
        quantity = input()

        products.update(name, {"price" : price, "quantity" : quantity})

def create_order(order):
    order_num = input("order num: ")
    
