vend = "Clare's Vend"
items = {
    "Drinks": {
        "A1": {"name": "Pepsi Cola", "price": 4.00, "stock": 3},
        "A2": {"name": "Coca Cola", "price": 4.00, "stock": 2},
        "A3": {"name": "Water", "price": 1.00, "stock": 3},
        "A4": {"name": "Pocari Sweat", "price": 6.00, "stock": 2},
    },
    "Chips": {
        "B1": {"name": "Lays", "price": 5.00, "stock": 4},
        "B2": {"name": "Cheetos", "price": 3.00, "stock": 4},
        "B3": {"name": "Oman Chips", "price": 1.50, "stock": 4},
        "B4": {"name": "Pringles", "price": 5.00, "stock": 4},
    },
    "Chocolate": {
        "C1": {"name": "Snickers", "price": 5.00, "stock": 3},
        "C2": {"name": "Twix", "price": 5.00, "stock": 3},
        "C3": {"name": "Cadburry Chocolate", "price": 5.00, "stock": 3},
        "C4": {"name": "Malteser", "price": 4.50, "stock": 3},
    }
}

suggestions = {
    "Drinks": ["B1", "B2", "C1"],
    "Chips": ["C3", "C4", "A3"],
    "Chocolate": ["A1", "B4", "A3"]
}

print(vend)
money = float(input('\nInsert your money: AED '))
print(f'You Inserted AED {money:.2f}')

while True:
    print('\n--- Options ---')
    for category, products in items.items():
        print(f'\n{category}:')
        for code, item in products.items():
            status = ('Out Of Stock'
                      if item['stock'] == 0

                      else 'Stock:', item['stock'])

            print(code,'-', item['name'], 'AED', item['price'], status)

    print(f'\nYou currently have AED {money:.2f}')
    choice = input("\nEnter item code: ").upper()

    selected = None
    s_cat = None

    # search for selected item
    for category, products in items.items():
        if choice in products:
            selected = products[choice]
            s_cat = category
            break

    if not selected:
        print('Invalid code.')
        continue

    if selected['stock'] == 0:
        print('Item out of stock.')
        continue

    # ensure enough money
    while money < selected['price']:
        print('Not enough money. You need AED', selected['price'], '.')
        add_more = input("Insert additional Money? (yes/no): ").lower()

        if add_more == "yes":
            extra = float(input("Insert additional Money: AED "))
            money += extra
            print(f"New Balance: AED {money:.2f}")
        else:
            print('Transaction cancelled.')
            print(f'Returning AED {money:.2f} change.')
            exit()

    # purchase item
    selected['stock'] -= 1
    money = round(money - selected['price'], 2)

    print('\nDispensing', selected['name'],'...')
    print(selected['name'], 'has been dispensed.')
    print(f'Remaining money: AED {money:.2f}')
    # show suggestions
    if s_cat in suggestions:
        print('\nSuggestions you may also like:')
        for s_code in suggestions[s_cat]:
            sug_item = None
            for cat, products in items.items():
                if s_code in products:
                    sug_item = products[s_code]
                    break
            if sug_item and sug_item['stock'] > 0:
                print(f' - {sug_item['name']} (Code: {s_code}) AED {sug_item['price']}')

    # ask user if they want to buy a suggested item
    buy_sug = input('\nWould you like to buy one of the suggested items? (yes/no): ').lower()

    if buy_sug == 'yes':
        ss_code = input('Enter suggestion code: ').upper()

        # Check if code is actually one of the suggested items for this category
        if ss_code not in suggestions[s_cat]:
            print('Invalid suggestion code. That item was not suggested.')
            again = input('\nBuy another item? (yes/no): ').lower()
            if again != 'yes':
                print(f'\nReturning AED {money:.2f} change.')
                print('Thank you for your purchase at', vend,'.')
                break
            else:
                continue

        # find the item in ANY category
        ss_item = None
        for category, products in items.items():
            if ss_code in products:
                ss_item = products[ss_code]
                break

        # checking if the input code is not on the item
        if not ss_item:
            print('Error: Suggested item not found in items list.')
            continue

        # Stock check
        if ss_item["stock"] == 0:
            print('Sorry,', ss_item['name'], 'is out of stock.')
            continue

        # Money check
        if money < ss_item["price"]:
            print(f'Not enough money for {ss_item['name']} (needs AED {ss_item['price']:.2f}.')
            more = input('Add more money? (yes/no): ').lower()

            if more == 'yes':
                extra = float(input('Insert additional Money: AED '))
                money += extra
                if money < ss_item['price']:
                    print('Still not enough. Returning to main menu.')
                    continue
            else:
                print('Returning to main menu.')
                continue

        # BUY SUGGESTED ITEM
        ss_item['stock'] -= 1
        money = round(money - ss_item['price'], 2)

        print('\nDispensing', ss_item['name'],'...')
        print(ss_item['name'],'has been dispensed.')
        print(f'\nReturning AED {money:.2f} change.')
        print('Thank you for your purchase at', vend, '.')
        exit()
    # ask if user wants to continue
    again = input('\nBuy another item? (yes/no): ').lower()
    if again != 'yes':
        print(f'\nReturning AED {money:.2f} change.')
        print('Thank you for your purchase at', vend, '.')
        break

