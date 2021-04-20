def sort(inventory):
    choice = 0
    for key in inventory[0]:
        print(key)
    print()
    choice = input("Type what you want to sort by: ")
    try:
        sorted_List = sorted(inventory, key=lambda k: k[choice.upper()]) 
        return sorted_List
    except:
        choice = 'ITEM'
        sorted_List = sorted(inventory, key=lambda k: k[choice.upper()]) 
        return sorted_List
def update(inventory):
    new_dictionary = {'ITEM': input("item name: "), 'QUANTITIY': input("item quantity: "), 'PRICE': input("item price: "), 'AVALIABLE': input("item avaliability: ")}
    inventory.append(new_dictionary)
    return inventory
def stock(inventory):
    for i in range(len(inventory)):
        print("current stock = " + str(inventory[i]['QUANTITIY'])) 
        inventory[i]['QUANTITIY'] += int(input("Stock Level change for " + str(inventory[i]['ITEM']) + ": "))
    return inventory
    
    
inventory = [
    # item name, quantity, price, avaliable
    {'ITEM': 'item2', 'QUANTITIY': 430, 'PRICE': 1.99, 'AVALIABLE': 'True'},
    {'ITEM': 'item1', 'QUANTITIY': 1240, 'PRICE': 23.99, 'AVALIABLE': 'True'},
    {'ITEM': 'item5', 'QUANTITIY': 420, 'PRICE': 1.20, 'AVALIABLE': 'False'},
    {'ITEM': 'item3', 'QUANTITIY': 41230, 'PRICE': 123.99, 'AVALIABLE': 'True'},
    {'ITEM': 'item4', 'QUANTITIY': 420, 'PRICE': 0.99, 'AVALIABLE': 'False'},
    ]
while True:
    print("Inventory Manager")
    print("-----------------")
    print("choices:")
    print("-Sort")
    print("-Update")
    print("-Stock")
    c = input("input choice: ")
    if c.lower() == "sort":
        print("-----------------")
        sorted = sort(inventory)
        for i in range(len(sorted)):
            print(sorted[i])
    if c.lower() == "update":
        print("-----------------")
        inventory = update(inventory)
        for i in range(len(inventory)):
            print(inventory[i])
    if c.lower() == "stock":
        print("-----------------")
        print("stock level changing, add (-) before num to reduce stock")
        print("-----------------")
        inventory = stock(inventory)
        for i in range(len(inventory)):
            print(inventory[i])
    
