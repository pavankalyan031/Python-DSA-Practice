#mini project
Menu={
    'Tea': 10,
    'Idle': 50,
    'Bonda': 30,
    'Puri': 40,
    'Dosa': 40
}

Customer_Name= input("May I Know Your Name?: ")
print(f"Hello {Customer_Name} Welcome to PAVAN'S Restaurant")
print("Menu List: \nTea : 10\nIdle: 50\nBonda: 30\nPuri: 40\nDosa: 40")


total=0
Item_1=""
Item_2=""
Item_1=input("Enter the name of the item want to order: ")
if Item_1 in Menu:
    total+=Menu[Item_1]
    print(f"Your Ordered {Item_1} is added to your orders")
else:
    print(f"Ordered {Item_1} is not on the Menu List!")

Another_Order= input("Do you want to order another Item?: (Yes/No): ")
if Another_Order == 'Yes':
    Item_2= input("Please Enter your order Item: ")
    if Item_2 in Menu:
        total+=Menu[Item_2]
        print(f"Your Ordered {Item_2} is added to your orders!")
    else:
        print(f"{Item_2} is not available")

print(f"Your Ordered Items are {Item_1} & {Item_2} and your total bill amount is {total}")
print(f"Thankyou {Customer_Name} for choosing PAVAN's Restaurant")




































