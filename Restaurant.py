MENU = [0, "King Cake Slice", "Croissant", "Catfish Po-boy", "Roast Beef Po-boy", "Sausage Po-boy", "Gumbo", "Crawfish Pie"]
MENU_COST = [0, 4.95, 3.95, 14.95, 13.95, 12.95, 5.95, 3.65]

CRAWFISH_WHOLE_PIE = 22

SALES_TAX = 0.0945
SHUTDOWN = False
total_cost = 0
usr_input = None

def menu():
    print("\n")
    print(f"Boudreaux & Thibodeaux's Restaurant \n--------------------------------------")
    print(f"1. {MENU[1]}: ${MENU_COST[1]} \n2. {MENU[2]}: ${MENU_COST[2]} \n3. {MENU[3]}: ${MENU_COST[3]} \n4. {MENU[4]}: ${MENU_COST[4]} \n5. {MENU[5]}: ${MENU_COST[5]} \n6. {MENU[6]}: ${MENU_COST[6]} \n7. Crawfish Pie (By the Slice): ${MENU_COST[7]}")
    print("--------------------------------------")
    
def crawfish_pies(usr_input,usr_input2, SALES_TAX=0.0945):
    counter = 0
    counter2 = 0
    crawfish_pie_order_cost = 0
    crawfish_slice_order_cost = 0

    while usr_input2 != 0:
        if usr_input2 >= 8:
            pie_tax = CRAWFISH_WHOLE_PIE * SALES_TAX
            crawfish_pie_order_cost += CRAWFISH_WHOLE_PIE + pie_tax
            counter += 1
            usr_input2 -= 8
        elif usr_input2 != 0 and usr_input2 < 8:
            slice_tax = MENU_COST[usr_input] * SALES_TAX
            crawfish_slice_order_cost += MENU_COST[usr_input] + slice_tax
            counter2 += 1
            usr_input2 -= 1


    text_CRAWFISH_WHOLE_PIE = CRAWFISH_WHOLE_PIE * counter
    text_CRAWFISH_SLICE = MENU_COST[usr_input] * counter2


    print(f"You have ordered {counter} Crawfish Pie for ${text_CRAWFISH_WHOLE_PIE:.2f}")
    print(f"You have ordered {counter2} Crawfish Slice for ${text_CRAWFISH_SLICE:.2f}")
    
    return crawfish_pie_order_cost + crawfish_slice_order_cost
            
            


def usr_order(usr_input,usr_input2, SALES_TAX=0.0945):
    order_cost = 0
    if usr_input2 < 1:
            print("Cannot order only 0 item, please put a valid whole number greater or equal to 1! ")
    elif usr_input2 > 0:
        if usr_input == 7:
            order_cost += crawfish_pies(usr_input,usr_input2, SALES_TAX=0.0945)
        else:
            print(f"You have ordered {usr_input2} {MENU[usr_input]} at ${MENU_COST[usr_input]} each")
            tax = ((MENU_COST[usr_input] * SALES_TAX) * usr_input2)
            order_cost += (MENU_COST[usr_input] * usr_input2) + tax
    else:
        print("Invalid Response")
    return order_cost






usr_input = None
menu()
usr_input = input("What would you like to order? Type the appropriate number of the menu item: ")

while SHUTDOWN != True:
    try:
        if usr_input.upper() == "DONE":
            SHUTDOWN = True
        elif usr_input == "1" or "2" or "3" or "4" or "5" or "6" or "7":
            
            usr_input = int(usr_input)
            usr_input2 = int(input("How many of that item would you like to order? "))
            
            total_cost += usr_order(usr_input,usr_input2)
            print(total_cost)
            menu()
            usr_input = input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete: ")

    except ValueError:
        menu()
        usr_input = input("Invalid Input, Please input a valid whole number from 1 - 7 or type DONE to complete order!: ")
            

print(f"\n Your Total is ${total_cost:.2f}")
            
        
        
        



