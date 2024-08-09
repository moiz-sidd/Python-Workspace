#define the menu of restaurant
menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'coffee':70,
    'salad':80,
}
#greet
print("Welcome To PYTHON Restaurant")
print("pizza: Rs40 \npasta: Rs40 \nBurger: Rs60 \ncoffe: Rs70 \nsalad: Rs80")

order_total = 0
another_order=""
while another_order != "No":

    item_1 = input("Enter the name of item you want to order = ")
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has ben added to your order")

    else:
        print(f"The order item '{item_1}'is not available. ")

    # ask if coustomer wants another item
    another_order = input( "Do you waant to order another item? (yes/no):")

# Print the total amount to pay 
print(f"The total amount to pay is: Rs{order_total}")
payment={
        
        'Cash'
        'Card'
}
print("Cash: \nCard:")
method = input("Enter the name of method in which you want to pay= ")
if method in payment:
    print(f"Your method {method} has ben added to your order")
    print("your transaction is done")