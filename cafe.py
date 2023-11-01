item1 = {"Product": 'Drip Coffee', "Price": 1.99}
item2 = {"Product": 'Cappuccino', "Price": 2.99}
item3 = {"Product": 'Smoothie', "Price": 7.50}
item4 = {"Product": 'Cookie', "Price": 1.99}
item5 = {"Product": 'Scone', "Price": 2.99}

menu = [item1, item2, item3, item4, item5]

drip_coffee_total = 0
cappucino_total = 0
smoothie_total = 0
cookie_total = 0
scone_total = 0

order_total = 0

def convert_tuple(menu_item):
    return f"{menu_item['Product']}: ${menu_item['Price']:.2f}"

def print_menu():
    print('**********\nCafe Menu\n**********\n')
    for item in menu:
        menu_item_str = convert_tuple(item) 
        print(menu_item_str)
    ordered_item = input('\n**********\nTo order a drink, simply type the item name and hit enter.\n')
    for item in menu:
        if item['Product'].lower() == ordered_item.lower():
            if item['Product'].lower() == 'drip coffee':
                drip_coffee_total += 1
                order_total += 1.99
            elif item['Product'].lower() == 'cappuccino':
                cappucino_total += 1
                order_total += 2.99
            elif item['Product'].lower() == 'smoothie':
                smoothie_total += 1
                order_total += 7.50
            elif item['Product'].lower() == 'cookie':
                cookie_total += 1
                order_total += 1.99
            elif item['Product'].lower() == 'scone':
                scone_total += 1
                order_total += 2.99
            else:
                print('Item not found.')
            print(f"Your order total is ${order_total:.2f}")
          

menu_greeting = input("Welcome to the Python Cafe!\n\n\nWould you like to see our menu? (Y/N) ")
if menu_greeting.lower() == 'y':
    print_menu()
else:
    print("Don't waste my time! Next, please.")
    tip_or_leave = input("\n\nTo leave the line, type 'Go'\nTo tip the barista $5 and see the menu, type 'Stay': ")
    if tip_or_leave.lower() == 'go':
        print("Thank you for your time.")
    elif tip_or_leave.lower() == 'stay':
        print_menu()
        order_total += 5
        print(f"Your order total is ${order_total:.2f}")
    else:
        print("Invalid choice. Goodbye!")
