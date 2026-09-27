items = ["Rice", "Wheat", "Milk", "Bread", "Eggs", "Curd"]
price = [40, 50, 55, 20, 70, 10]
cart_items = []
cart_amt = []
subtotal=0
discount=0
grand=0
def displayitems():
    print("\n=======AVAILABLE ITEMS========")
    for i in range(len(items)):
        print(i+1, ")", items[i], " - Rs.", price[i])
    print("==============================\n")

def additem():
    displayitems()
    
    choice = int(input("Enter the display number: "))
    quant = int(input("Enter the quantity: "))

    cart_items.append(choice)
    cart_amt.append(quant)
    print("\n==============================")
    print(items[choice-1], "added to your cart, amount=>", quant)
    print("==============================\n")

def viewcart(subtotal):
    print("\n==========YOUR CART===========")
    print(cart_items)
    print(cart_amt)
    for i in range(len(cart_items)):
        item_name = items[cart_items[i]-1]
        price1 = price[cart_items[i]-1]

        total = (price1)*(cart_amt[i])

        print(i+1,".",item_name,"-",cart_amt[i],"X Rs.",price1,"=",total)
        subtotal = subtotal+total
    print("\n=================================")
    print("The final billing amount=> ",subtotal)
    print("=================================\n")
    return subtotal

def removecart(subtotal):
    viewcart(subtotal)
    choice = int(input("Enter the item number from bill you want to remove: "))
    if choice <= (len(cart_items)):
        cart_items.pop(choice-1)
        cart_amt.pop(choice-1)
        print("Item removed")
    else:
        print("Invalid choice")
    viewcart(subtotal)


while True:
    print("\n=============GROCERY STORE==============")
    print("1. Display available items")
    print("2. Add item to cart")
    print("3. View cart and bill")
    print("4. Remove item from cart")
    print("5. Exit")
    print("=========================================")
    n = int(input("\nEnter your choice: "))

    if n==1:
        displayitems()
    elif n==2:
        additem()
    elif n==3:
        viewcart(subtotal)
    elif n==4:
        removecart(subtotal)
    elif n==5:
       break
    else:
        print("Invalid choice")