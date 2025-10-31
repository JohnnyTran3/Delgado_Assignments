MENU = [0, "Muffin", "King Cake Slice", "Croissant", "Scone"]
MENU_COST = [0, 5.95, 4.95, 3.95, 3.75]


SALES_TAX = 0.0945
SHUTDOWN = False
total_cost = 0

print(f"Boudreaux & Thibodeaux's Bakery \n--------------------------------------")


print(f"1. Muffin: {MENU_COST[1]} \n1. King Cake Slice: {MENU_COST[2]} \n2. Croissant: {MENU_COST[3]} \n3. Scone: {MENU_COST[4]}\n--------------------------------------")


while SHUTDOWN != True:
    usr_input = input("What would you like to order? Please type a whole number from 1 - 4!: ")
    if usr_input.isalpha():
        print("Invalid Input, Please input a valid whole number from 1 - 4: ")
    else:
        usr_input = int(usr_input)
        while usr_input >= 1 or usr_input <= 4:
            usr_input2 = int(input("How many of that item would you like to order? "))
            if usr_input2 < 1:
                print("Cannot order only 0 item, please put a valid whole number greater or equal to 1! ")
                usr_input2 = int(input("How many of that item would you like to order?"))
            if usr_input2 > 0:
                print(f"You have ordered {usr_input2} {MENU[usr_input]} for {MENU_COST[usr_input]}")
                total_cost += (MENU_COST[usr_input] * usr_input2)
                print(total_cost)
            usr_input = int(input("What would you like to order? Please type a whole number from 1 - 4 or type 999 when order is complete!: "))
            
    if usr_input == 999:
        SHUTDOWN = True
    else:
        while usr_input < 1 or usr_input > 4:
            print("Invalid Input, Please input a valid whole number from 1 - 4 or type 999 to complete order!: ")


print(f"Your Total is {total_cost}")
            
        
        
        



