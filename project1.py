from datetime import datetime

name = input("Enter your name: ")

# List of items
items_list = '''
Rice     Rs 20/kg
Sugar    Rs 30/kg
Salt     Rs 20/kg
Oil      Rs 80/liter
Paneer   Rs 110/kg
Maggi    Rs 50/kg
Boost    Rs 90/each
Colgate  Rs 85/each
'''

# Price dictionary (use lowercase keys for consistency)
items = {
    'rice': 20,
    'sugar': 30,
    'salt': 20,
    'oil': 80,
    'paneer': 110,
    'maggi': 50,
    'boost': 90,
    'colgate': 85
}

# Data collection lists
pricelist = []
ilist = []
qlist = []
plist = []

totalprice = 0

# Show item list if needed
option = int(input("For list of items press 1: "))
if option == 1:
    print(items_list)

# Buying loop
while True:
    choice = int(input("Press 1 to buy item, 2 to exit: "))
    if choice == 2:
        break
    elif choice == 1:
        item = input("Enter the item name: ").lower()
        quantity = int(input("Enter quantity: "))
        if item in items:
            price = quantity * items[item]
            pricelist.append((item, quantity, price))
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            totalprice += price
        else:
            print("Sorry, the item is not available.")
    else:
        print("Invalid input, try again.")

# If items were purchased, show bill
if totalprice != 0:
    gst = round(totalprice * 0.05, 2)
    finalamount = totalprice + gst

    print("="*25, "Sabiha Supermarket", "="*25)
    print(" "*28, "Yeleswaram")
    print("Name:", name, " "*25, "Date:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("-"*75)
    print("S.No", " "*5, "Item", " "*10, "Qty", " "*5, "Price")
    print("-"*75)

    for i in range(len(pricelist)):
        print(i+1, " "*8, ilist[i].capitalize(), " "*8, qlist[i], " "*7, plist[i])

    print("-"*75)
    print(" "*50, "Total: Rs", totalprice)
    print(" "*50, "GST (5%): Rs", gst)
    print("-"*75)
    print(" "*50, "Final Amount: Rs", finalamount)
    print("="*75)
    print(" "*25, "Thank you for visiting!")
    print("="*75)
else:
    print("No items purchased.")
input("\nPress Enter to exit...")
