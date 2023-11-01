item1 = {"Product": 'Drip Coffee', "Price": 1.99}
item2 = {"Product": 'Cappuccino', "Price": 2.99}
item3 = {"Product": 'Smoothie', "Price": 7.50}
item4 = {"Product": 'Cookie', "Price": 1.99}
item5 = {"Product": 'Scone', "Price": 2.99}

menu = [item1, item2, item3, item4, item5]

def convert_tuple(menu_item):
    return f"{menu_item['Product']}: ${menu_item['Price']:.2f}"

def print_menu():
    print('**********\nCafe Menu\n**********')
    for item in menu:
        menu_item_str = convert_tuple(item) 
        print(menu_item_str)

print_menu()