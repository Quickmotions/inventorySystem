import csv
def sort(inventory):
    choice = 0
    for key in inventory[0]:
        print(key)
    print()
    choice = input("Type what you want to sort by: ")
    try:
        sorted_List = sorted(inventory, key=lambda k: k[choice.upper()])
        UpdateCSV(inventory)
        return sorted_List
    except:
        choice = 'ITEM'
        sorted_List = sorted(inventory, key=lambda k: k[choice.upper()])
        UpdateCSV(inventory)
        return sorted_List
def update(inventory):
    new_dictionary = {'ITEM': input("item name: "), 'QUANTITIY': input("item quantity: "), 'PRICE': input("item price: "), 'AVALIABLE': input("item avaliability: ")}
    inventory.append(new_dictionary)
    UpdateCSV(inventory)
    return inventory

def stock(inventory):
    for i in range(len(inventory)):
        print("current stock = " + str(inventory[i]['QUANTITIY'])) 
        inventory[i]['QUANTITIY'] += int(input("Stock Level change for " + str(inventory[i]['ITEM']) + ": "))
    UpdateCSV(inventory)
    return inventory

def remove(inventory):
    
    x = int(input("enter line number to remove(0 for none): ")) -1
    if x == "0":
        return inventory
    else:
        inventory.remove(inventory[x])
        UpdateCSV(inventory)
        return inventory

def UpdateCSV(inventory):
    with open('inventory.csv', 'w', newline ='') as file:  
        header = ['ITEM', 'QUANTITIY', 'PRICE', 'AVALIABLE']
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        for i in range(len(inventory)):
            writer.writerow(inventory[i])
inventory = []
with open('inventory.csv', 'r') as file:
    dictionary = dict()
    for line in file.readlines()[1:]:
        split = line.split(",")
        split[3] = split[3][:-1]
        dictionary = {'ITEM': split[0], 'QUANTITIY': int(split[1]), 'PRICE': float(split[2]), 'AVALIABLE': split[3]}
        inventory.append(dictionary)

while True:
    print("Inventory Manager")
    print("-----------------")
    print("choices:")
    print("[1]-Sort")
    print("[2]-Add")
    print("[3]-Stock")
    print("[4]-View")
    print("[5]-Remove")
    c = ""
    c = input("input choice: ")
    if c.lower() == "sort" or c.lower() == "1":
        print("-----------------")
        sorted = sort(inventory)
        for i in range(len(sorted)):
            print(sorted[i])
    if c.lower() == "add" or c.lower() == "2":
        print("-----------------")
        inventory = update(inventory)
        for i in range(len(inventory)):
            print(inventory[i])
    if c.lower() == "stock" or c.lower() == "3":
        print("-----------------")
        print("stock level changing, add (-) before num to reduce stock")
        print("-----------------")
        inventory = stock(inventory)
        for i in range(len(inventory)):
            print(inventory[i])
    if c.lower() == "view" or c.lower() == "4":
        print("-----------------")
        for i in range(len(inventory)):
            print(inventory[i])
    if c.lower() == "remove" or c.lower() == "5":
        print("-----------------")
        for i in range(len(inventory)):
            print(i+1 , " : ", inventory[i])
        print("-----------------")
        inventory = remove(inventory)
        for i in range(len(inventory)):
            print(inventory[i])
   
            
