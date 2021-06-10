import csv
from datetime import date, datetime
def sort(inventory,sales):
    sortRoot = tk.Tk()
    titleText = tk.Label(sortRoot,text="Inventory Managment System (v1.0)")
    gridText = ""
    for i in range(len(inventory)):
        gridText += str(inventory[i]) + "\n"
    inventoryGrid = tk.Label(sortRoot, 
                        text=gridText, 
                        borderwidth = 3,
                        relief="sunken",
                        justify="left")
    itemButton = tk.Button(sortRoot,borderwidth = 3,  text="Sort Name", command=lambda: sortBy (sortRoot,inventoryGrid,inventory, "ITEM"))
    quantitiyButton = tk.Button(sortRoot,borderwidth = 3,  text="Sort Quantity", command=lambda: sortBy (sortRoot,inventoryGrid,inventory,"QUANTITIY"))
    priceButton = tk.Button(sortRoot,borderwidth = 3,  text="Sort Price", command=lambda: sortBy (sortRoot,inventoryGrid,inventory,"PRICE"))
    avaliableButton = tk.Button(sortRoot,borderwidth = 3,  text="Sort Avaliability", command=lambda: sortBy (sortRoot,inventoryGrid,inventory,"AVALIABLE"))
    backButton = tk.Button(sortRoot,borderwidth = 3,  text="Back", command=lambda: returnMain(sortRoot,inventory,sales))

    backButton.grid(row=3,column=4)
    titleText.grid(row=1)
    inventoryGrid.grid(row=2)
    itemButton.grid(row = 2, column=1)
    quantitiyButton.grid(row=2, column=2)
    priceButton.grid(row=2,column=3)
    avaliableButton.grid(row=2, column=4)
    inventoryGrid.mainloop()

def returnMain(sortRoot,inventory,sales):
    sortRoot.quit()
    sortRoot.destroy()
    createUI(inventory,sales)

def sortBy(sortRoot,inventoryGrid,inventory, num):
    inventoryGrid.destroy()
    sorted_List = sorted(inventory, key=lambda k: k[num.upper()])
    UpdateCSV(inventory,sales)
    gridText = ""
    for i in range(len(sorted_List)):
        gridText += str(sorted_List[i]) + "\n"
    inventoryGrid = tk.Label(sortRoot, 
                        text=gridText, 
                        borderwidth = 3,
                        relief="sunken",
                        justify="left")
    inventoryGrid.grid(row=2)

def update(inventory,sales):
    updateRoot = tk.Tk()
    titleText = tk.Label(updateRoot,text="Inventory Managment System (v1.0)")
    itemLabel = tk.Label(updateRoot,borderwidth = 3, text="Item Name:")
    itemInput = tk.Entry(updateRoot,borderwidth = 3)
    quantitityLabel = tk.Label(updateRoot,borderwidth = 3, text="Item Quantity:")
    quantitityInput = tk.Entry(borderwidth = 3)
    priceLabel = tk.Label(updateRoot,borderwidth = 3, text="Item Price:")
    priceInput = tk.Entry(updateRoot,borderwidth = 3)
    avaliableLabel = tk.Label(updateRoot,borderwidth = 3, text="Item Avaliability:")
    avaliableInput = tk.Entry(updateRoot,borderwidth = 3)
    inputButton = tk.Button(updateRoot,borderwidth = 3,  text="Enter", command=lambda: updateInv(inventory,itemInput,quantitityInput,priceInput,avaliableInput))
    backButton = tk.Button(updateRoot,borderwidth = 3,  text="Back", command=lambda: returnMain(updateRoot,inventory,sales))

    titleText.grid(row=1)
    itemLabel.grid(row=2)
    itemInput .grid(row=2, column=1)
    quantitityLabel.grid(row=3)
    quantitityInput.grid(row=3, column=1)
    priceLabel.grid(row=4)
    priceInput.grid(row=4,column=1)
    avaliableLabel.grid(row=5)
    avaliableInput.grid(row=5,column=1)

    inputButton.grid(row= 2, column=3)
    backButton.grid(row=3, column=3)
    updateRoot.mainloop()
    


def updateInv(inventory,itemInput,quantitityInput,priceInput,avaliableInput):
    new_dictionary = {'ITEM': itemInput.get(), 'QUANTITIY': int(quantitityInput.get()) , 'PRICE': int(priceInput.get()) , 'AVALIABLE': avaliableInput.get()}
    inventory.append(new_dictionary)
    UpdateCSV(inventory,sales)

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
    
    print("Income = " + str(round(price, 2)))
    print("New Total = " + str(round(sales[len(sales)-1]['TOTAL'] + int(price),2)))
    
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

def sortButtonPress(sales, inventory,root):
        root.destroy()
        sort(inventory,sales)
def addButtonPress(sales, inventory,root):
        root.destroy()
        update(inventory,sales)

def stockButtonPress(sales, inventory,root):
        root.destroy()
        stock(inventory, sales)
       
def valueButtonPress(sales, inventory,root):
        
        value(sales,inventory)

def removeButtonPress(sales, inventory,root):
        
        for i in range(len(inventory)):
            print(i+1 , " : ", inventory[i])
        
        inventory = remove(inventory)
        for i in range(len(inventory)):
            print(inventory[i])
def statsButtonPress(sales, inventory,root):
        
        print("Average Income: " + str(findAVG(sales)))
        print("Total Income: " + str(findTOTAL(sales)))
        
        

def createUI(inventory,sales):
    root = tk.Tk()
    global labelText
    gridText = ""
    title = tk.Label(text="Inventory Managment System (v1.0)")
    for i in range(len(inventory)):
        gridText += str(inventory[i]) + "\n"
    inventoryGrid = tk.Label(root, 
                        text=gridText, 
                        borderwidth = 3,
                        relief="sunken",
                        justify="left")
    salesText = ""
    for i in range(len(sales)):
        salesText += str(sales[i]) + "\n"
    salesGrid = tk.Label(root, 
                        text=gridText, 
                        borderwidth = 3,
                        relief="sunken",
                        justify="left")
    sortButton = tk.Button(borderwidth = 3, text="Sort", command=lambda: sortButtonPress (sales,inventory,root))
    addButton = tk.Button(borderwidth = 3, text="Add", command=lambda: addButtonPress (sales,inventory,root))
    stockButton = tk.Button(borderwidth = 3,  text="Stock", command=lambda: stockButtonPress (sales,inventory,root))
    valueButton = tk.Button(borderwidth = 3,  text="Value", command=lambda: valueButtonPress (sales,inventory,root))
    removeButton = tk.Button(borderwidth = 3, text="Remove", command=lambda: removeButtonPress (sales,inventory,root))
    statsButton = tk.Button(borderwidth = 3,  text="Stats", command=lambda: statsButtonPress (sales,inventory,root))
    
    sortButton.grid(row=3, column=1 )
    addButton.grid(row=3, column=2 )
    stockButton.grid(row=3, column=3 )
    valueButton.grid(row=3, column=4 )
    removeButton.grid(row=3, column=5 )
    statsButton.grid(row=3, column=6 )
    title.grid(row=1)
    inventoryGrid.grid(row=2)
    salesGrid.grid(row=3)
    root.mainloop()
global inventory
global sales
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

import tkinter as tk
createUI(inventory, sales)
            
