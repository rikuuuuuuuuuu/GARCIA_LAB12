# Christofferson Kyle C. Garcia
# IT-102

# display menu function
def display_menu():
    # list of menu items and prices
    menu = [
        {"item": "burger", "price": 50},
        {"item": "pizza", "price": 120},
        {"item": "soda", "price": 30}
    ]

    # print menu
    print("menu:")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]['item']} - php {menu[i]['price']}")

    # return menu for later use
    return menu

# select order function
def select_order(menu):
    while True:
        # input selection
        choice = int(input("select item number from menu: ")) - 1
        
        # validate choice
        if 0 <= choice < len(menu):
            return menu[choice]
        else:
            print("invalid choice. try again.")

# calculate payment function
def process_payment(total):
    while True:
        # input cash rendered
        cash = int(input("enter cash amount: "))
        
        # check if cash is enough
        if cash >= total:
            change = cash - total
            return change
        else:
            print("insufficient cash. try again.")

# main program function
def main():
    # display menu
    menu = display_menu()

    # select order
    selected_item = select_order(menu)
    print(f"you selected {selected_item['item']} costing php {selected_item['price']}.")

    # calculate payment
    change = process_payment(selected_item['price'])
    print(f"payment successful. change: php {change}")

# execute program
main()
