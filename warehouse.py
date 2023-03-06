import sys
import csv

items = [
    {'name': 'Apple', 'quantity': '25', 'unit': 'kg', 'unit_price': '30'},
    {'name': 'Banana', 'quantity': '18', 'unit': 'kg', 'unit_price': '45'},
    {'name': 'Orange', 'quantity': '20', 'unit': 'kg', 'unit_price': '60'}
]

csv_path = "C:/Users/Proffessional/Desktop/Kodilla/store/magazyn.csv"
def export_items_to_csv():
    with open ('magazyn.csv', mode='w') as csv_file:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)
        print ("Successfully exported data to magazyn.csv")

def load_items_from_csv(csv_path):
    items.clear()
    with open (csv_path, mode= 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            items.append(row)
    print ("Successfully loaded data from magazyn.csv")
    return items

if __name__ == "__main__":
    csv_path = sys.argv[1]  
    items = load_items_from_csv(csv_path)
    print(items)
        
sold_items = [ ]

def get_items(): 
    print("Name", "Quantity", "Unit", "Unit Price", sep ="  ")
    print("----", "--------", "----", "----------", sep ="  ")
    for f in items:
       print (f["name"], f["quantity"], f["unit"], f["unit_price"], sep = "\t")

def add_item():
    name = input("Enter item name:")
    quantity = int(input("Enter item quantity:"))
    unit = input("Enter item unit:")
    unit_price = int(input("Enter item price:"))
    new_item = {'name': name, 'quantity': quantity, 'unit': unit, 'unit_price': unit_price}
    items.append(new_item)
    print (f"Successfully added to warehouse.Current status:")
    get_items()
    
def sell_item():
    sell_name = input("Enter item to sell: ")
    sell_quantity = float(input("Enter quantity to sell: "))
    sell_unit = input("Enter unit of item to sell: ") 
    sell_unit_price = input("Enter unit price of item to sell: ") 
    for item in items:
        if sell_name == item['name']:
            item['quantity'] = float(item['quantity']) - sell_quantity
            item['unit'] = item['unit']
            item['unit_price'] = item['unit_price']
            get_items()
            sold_items.append({'name': sell_name, 'quantity': sell_quantity, 'unit': sell_unit, 'unit_price': sell_unit_price})
            return
    print (f"Successfully sold {sell_quantity} {sell_unit} of {sell_name}") 

def get_costs():
    costs = [float(item['quantity']) * float(item['unit_price']) for item in items]
    return sum(costs)

def get_income():
    income = [float(item['quantity']) * float(item['unit_price']) for item in sold_items]
    return sum(income)

def show_revenue():
    costs = get_costs()
    income = get_income()
    revenue = income - costs
    print ("Revenue breakdown (PLN)")
    print (f"Income:  {income}")
    print (f"Costs: {costs}")
    print ("------")
    print (f"Revenue: {revenue}")
    return revenue

action = " "
while action != "exit":
    action = input("What would you like to do? (enter help for other information) ")
    if action in ('exit', 'help', 'show', 'showsold', 'add', 'sell', 'show_revenue', 'load', 'save'):
        if action == "help":
            print("Make your choice: show, add, sell, showsold, show_revenue, save, load or exit")
        if action == "add":
            add_item()
        if action == "show":
            get_items()
        if action == "sell":
            sell_item()
        if action == "showsold":
            print(sold_items)
        if action == "show_revenue":
            show_revenue()
        if action == "save":
            export_items_to_csv()
        if action == "load":
            load_items_from_csv()
        if action == "exit":
            print("Exiting... Bye-bye!")
            exit()
    else:
        print("Oops, wrong choice. Please enter again.")

        
       



