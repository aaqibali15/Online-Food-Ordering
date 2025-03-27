menu = {
    "Burger" : 350,
    "Pizza" : 500,
    "Sharwama" : 200,
    "Roll" : 220
}

def display_menu():
    for key,value in menu.items():
        print(f"Item: {key}, Price: { value}")
### input fucntion
def user_input(prompt):
    return input(prompt)

####  take order
def order_place():
    user_order= {}
    while True:
        order = user_input("Enter you items(and write done for finish the order):")
        if order in menu:
            try:
                quantity= int(user_input(f"Please enter quantity of {order}:"))
                user_order[order] = quantity
            except:
                print("Write proper quantity")
        
        elif order == "done":
            break
        else:
            print("This item not available")
    print(user_order)
    return user_order

#####3  bill calculate
def bill_calculate(user_order):
    total_bill = 0
    for key,values in user_order.items():
        total_bill += menu[key] * values
    print("Total Price is:",total_bill)
    
    
    

##########   main 
display_menu()
bill = order_place()
bill_calculate(bill)