catfish_poboy_cost = 14.95
roast_beef_poboy_cost = 13.95
sausage_poboy_cost = 12.95
gumbo_cost = 4.95



print(f"1. Catfish Poboy: ${catfish_poboy_cost}")
print(f"2. Roast Beef Poboy: ${roast_beef_poboy_cost}")
print(f"3. Sausage Poboy: ${sausage_poboy_cost}")
print(f"4. Catfish : ${gumbo_cost}")



item_wanted = float(input("What would you like to order? Type the appropriate number of the menu item: "))



if item_wanted == 1:
    total_cost = (catfish_poboy_cost * 0.0945) + catfish_poboy_cost
    print(f"Your total is ${total_cost:.2f}")
elif item_wanted == 2:
    total_cost = (roast_beef_poboy_cost * 0.0945) + roast_beef_poboy_cost
    print(f"Your total is ${total_cost:.2f}")
elif item_wanted == 3:
    total_cost = (sausage_poboy_cost * 0.0945) + sausage_poboy_cost
    print(f"Your total is ${total_cost:.2f}")
elif item_wanted == 4:
    total_cost = (gumbo_cost * 0.0945) + gumbo_cost
    print(f"Your total is ${total_cost:.2f}")
else:
    print("Unknown meal item, Please try again.")