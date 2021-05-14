import csv
from datetime import date, datetime
def sort(inventory):
    choice = 0
    for key in inventory[0]:
        print(key)
    print()
    choice = input("Type what you want to sort by: ")
    try:
        sorted_List = sorted(inventory, key=lambda k: k[choice.upper()])
        UpdateCSV(inventory,sales)
        return sorted_List
    except:
        choice = 'ITEM'
        sorted_List = sorted(inventory, key=lambda k: k[choice.upper()])
        UpdateCSV(inventory,sales)
        return sorted_List
def update(inventory):
    new_dictionary = {'ITEM': input("item name: "), 'QUANTITIY': input("item quantity: "), 'PRICE': input("item price: "), 'AVALIABLE': input("item avaliability: ")}
    inventory.append(new_dictionary)
    UpdateCSV(inventory,sales)
    return inventory
def value(sales,inventory):
    money = input("change in value ( - for loss): ")
    newValue = {'TOTAL': round(sales[len(sales)-1]['TOTAL'] + int(money), 2), 'INCOME': round(int(money), 2), 'DATE': date.today().strftime("%d/%m/%Y"), 'TIME': datetime.now().strftime("%H:%M:%S")} 
    sales.append(newValue)
    UpdateCSV(inventory,sales)
    return sales,inventory
def stock(inventory, sales):
    price = 0
    for i in range(len(inventory)):
        print("current stock = " + str(inventory[i]['QUANTITIY']))
        level = int(input("Stock Level change for " + str(inventory[i]['ITEM']) + ": "))
        if(level < 0):
            price += inventory[i]['PRICE'] * level * -1
        inventory[i]['QUANTITIY'] += level
    newSale = {'TOTAL': round(sales[len(sales)-1]['TOTAL'] + int(price), 2), 'INCOME': round(int(price), 2), 'DATE': date.today().strftime("%d/%m/%Y"), 'TIME': datetime.now().strftime("%H:%M:%S")} 
    sales.append(newSale)
    UpdateCSV(inventory,sales)
    print("-----------------")
    print("Income = " + str(round(price, 2)))
    print("New Total = " + str(round(sales[len(sales)-1]['TOTAL'] + int(price),2)))
    print("-----------------")
    return inventory, sales

def remove(inventory):
    
    x = int(input("enter line number to remove(0 for none): ")) -1
    if x == "0":
        return inventory
    else:
        inventory.remove(inventory[x])
        UpdateCSV(inventory,sales)
        return inventory
def UpdateCSV(inventory,sales):
    with open('inventory.csv', 'w', newline ='') as file:  
        header = ['ITEM', 'QUANTITIY', 'PRICE', 'AVALIABLE']
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        for i in range(len(inventory)):
            writer.writerow(inventory[i])
    with open('sales.csv', 'w', newline ='') as file:  
        header = ['TOTAL', 'INCOME', 'DATE', 'TIME']
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        for i in range(len(sales)):
            writer.writerow(sales[i])
def findAVG(sales):
    count = 0
    average = 0
    for i in range(len(sales)):
        average += int(sales[i]['INCOME'])
        count += 1
    average = round(average / count)
    return average
def findTOTAL(sales):
    total = 0
    for i in range(len(sales)):
        total += int(sales[i]['INCOME'])
    return total
inventory = []
sales = []
with open('inventory.csv', 'r') as file:
    dictionary = dict()
    for line in file.readlines()[1:]:
        split = line.split(",")
        split[3] = split[3][:-1]
        dictionary = {'ITEM': split[0], 'QUANTITIY': int(split[1]), 'PRICE': float(split[2]), 'AVALIABLE': split[3]}
        inventory.append(dictionary)
with open('sales.csv', 'r') as file:
    dictionary = dict()
    for line in file.readlines()[1:]:
        split = line.split(",")
        split[3] = split[3][:-1]
        dictionary = {'TOTAL': int(split[0]), 'INCOME': int(split[1]), 'DATE': split[2], 'TIME': split[3]}
        sales.append(dictionary)

while True:
    print("choices: [1]-Sort     [2]-Add     [3]-Stock    [4]-View   [5]-Value   [6]-Sales    [7]-Remove    [8]-Stats")
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
        inventory, sales = stock(inventory, sales)
        for i in range(len(inventory)):
            print(inventory[i])
    if c.lower() == "view" or c.lower() == "4":
        print("-----------------")
        for i in range(len(inventory)):
            print(inventory[i])
    if c.lower() == "value" or c.lower() == "5":
        print("-----------------")
        sales,inventory = value(sales,inventory)
        for i in range(len(sales)):
            print(sales[i])
    if c.lower() == "sales" or c.lower() == "6":
        print("-----------------")
        for i in range(len(sales)):
            print(sales[i])
    if c.lower() == "remove" or c.lower() == "7":
        print("-----------------")
        for i in range(len(inventory)):
            print(i+1 , " : ", inventory[i])
        print("-----------------")
        inventory = remove(inventory)
        for i in range(len(inventory)):
            print(inventory[i])
    if c.lower() == "stats" or c.lower() == "8":
        print("-----------------")
        print("Average Income: " + str(findAVG(sales)))
        print("Total Income: " + str(findTOTAL(sales)))
        print("-----------------")
        
            
            
