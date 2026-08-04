# ---------- Preloaded Inventory ---------- 

inventory = { 

    "101": {"name": "Nescafe Coffee Gold Blend (200g)", "price": 620, "quantity": 15}, 

    "102": {"name": "Lindt Swiss Chocolate (100g)", "price": 480, "quantity": 20}, 

    "103": {"name": "Nutella Hazelnut Spread (750g)", "price": 850, "quantity": 18}, 

    "104": {"name": "Ferrero Rocher (24 Pack)", "price": 950, "quantity": 10}, 

    "105": {"name": "Imported Olive Oil (1L)", "price": 1200, "quantity": 12}, 

    "106": {"name": "Oreo Chocolate Cake Mix", "price": 350, "quantity": 25}, 

    "107": {"name": "Tropicana Mixed Fruit Juice (2L)", "price": 230, "quantity": 30}, 

    "108": {"name": "Red Label Natural Care Tea (1kg)", "price": 480, "quantity": 25}, 

    "109": {"name": "Organic Almonds (1kg)", "price": 950, "quantity": 16}, 

    "110": {"name": "Hershey’s Chocolate Syrup (623g)", "price": 310, "quantity": 20}, 

    "111": {"name": "Imported Green Tea (Assorted Pack)", "price": 720, "quantity": 15}, 

    "112": {"name": "Luxury Scented Candle Set", "price": 890, "quantity": 12}, 

    "113": {"name": "Dark Fantasy Cookies (Premium Pack)", "price": 290, "quantity": 25}, 

    "114": {"name": "Lays Chips", "price": 20, "quantity": 50}, 

    "115": {"name": "Maggie Noodles", "price": 15, "quantity": 80} 

} 

 

# ---------- Sales List ---------- 
import datetime

sales = [] 

 

# ---------- Core Functions ---------- 

def add_item(): 

    item_id = input("Enter Item ID: ") 

    if item_id in inventory: 

        print("Item ID already exists!") 

        return 

    name = input("Enter Item Name: ") 

    price = float(input("Enter Item Price: ")) 

    quantity = int(input("Enter Item Quantity: ")) 

    inventory[item_id] = {"name": name, "price": price, "quantity": quantity} 

    print(f"{name} added successfully!") 

 
def update_item():

    item_id = input("Enter Item ID to update: ")

    if item_id not in inventory:

        print("Item not found!")
        return

    print("Leave blank if you don't want to change a field.")
    name = input(f"Enter new name ({inventory[item_id]['name']}): ") or inventory[item_id]['name']

    try:
        price = input(f"Enter new price ({inventory[item_id]['price']}): ")
        price = float(price) if price else inventory[item_id]['price']
    except ValueError:
        price = inventory[item_id]['price']

    try:
        qty = input(f"Enter new quantity ({inventory[item_id]['quantity']}): ")
        qty = int(qty) if qty else inventory[item_id]['quantity']
    except ValueError:
        qty = inventory[item_id]['quantity']

    inventory[item_id] = {"name": name, "price": price, "quantity": qty}
    print("Item updated successfully!")
print("Item updated successfully!")

 

def delete_item(): 

    item_id = input("Enter Item ID to delete: ") 

    if item_id in inventory: 

        del inventory[item_id] 

        print("Item deleted successfully!") 

    else: 

        print("Item not found!") 

 

def view_inventory(): 

    if not inventory: 

        print("Inventory is empty.") 

        return 

    print("\nCurrent Inventory:") 

    print("-" * 60) 

    for item_id, details in inventory.items(): 

        print(f"ID: {item_id} | Name: {details['name']} | Price: ₹{details['price']} | Qty: {details['quantity']}") 

    print("-" * 60) 

 
def sell_item():

    item_id = input("Enter Item ID to sell: ")

    if item_id not in inventory:

        print("Item not found!")
        return

    try:
        qty = int(input("Enter quantity to sell: "))
    except ValueError:
        print("Invalid quantity.")
        return

    if qty > inventory[item_id]['quantity']:

        print("Not enough stock!")
        return

    inventory[item_id]['quantity'] -= qty

    total_price = qty * inventory[item_id]['price']

    sale_record = {
        "item_id": item_id,
        "name": inventory[item_id]['name'],
        "qty": qty,
        "total": total_price,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    sales.append(sale_record)
    print(f"Sold {qty} x {inventory[item_id]['name']} for ₹{total_price}")
    print(f"Sold {qty} x {inventory[item_id]['name']} for ₹{total_price}") 

 

def daily_sales_report(): 

    if not sales: 

        print("No sales made yet.") 

        return 

    print("\nDaily Sales Report") 

    print("-" * 60) 

    total_revenue = 0 

    for sale in sales: 

        print(f"{sale['time']} | {sale['name']} | Qty: {sale['qty']} | ₹{sale['total']}") 

        total_revenue += sale['total'] 

    print("-" * 60) 

    print(f"Total Revenue: ₹{total_revenue}") 

 

def low_stock_alert(): 

    print("\nLow Stock Alert:") 

    found = False 

    for item_id, details in inventory.items(): 

        if details['quantity'] <= 10: 

            print(f"ID: {item_id} | {details['name']} | Qty Left: {details['quantity']}") 

            found = True 

    if not found: 

        print("All items sufficiently stocked.") 

    print("-" * 60) 

 

def generate_bill(): 

    print("\nGenerate Bill / Invoice") 

    bill_items = [] 

    total = 0 

    while True: 

        item_id = input("Enter item ID (or 'done' to finish): ") 

        if item_id.lower() == 'done': 

            break 

        if item_id in inventory: 

            qty = int(input("Enter quantity: ")) 

            if qty <= inventory[item_id]['quantity']: 

                cost = qty * inventory[item_id]['price'] 

                bill_items.append((inventory[item_id]['name'], qty, inventory[item_id]['price'], cost)) 

                inventory[item_id]['quantity'] -= qty 

                total += cost 

            else: 

                print("Not enough stock.") 

        else: 

            print("Invalid item ID.") 

    print("\n----------- BILL -----------") 

    for name, qty, price, cost in bill_items: 

        print(f"{name} x{qty} @ ₹{price} = ₹{cost}") 

    print("-----------------------------") 

    print(f"Total Amount: ₹{total}") 

    print("-----------------------------") 

 

def discount_manager(): 

    print("\nDiscount Manager") 

    discount = float(input("Enter discount percentage: ")) 

    for item in inventory.values(): 

        item['price'] -= (item['price'] * discount / 100) 

    print(f"{discount}% discount applied to all items.") 

    print("-" * 60) 

 

print("=" * 60) 

print("Welcome to Valencia Shop Management System") 

print("=" * 60) 

print("Hello! This system will help you manage your shop easily.\n") 

 

while True: 

    print("\nMain Menu:") 

    print("1. Add Item") 

    print("2. Update Item") 

    print("3. Delete Item") 

    print("4. View Inventory") 

    print("5. Sell Item") 

    print("6. Daily Sales Report") 

    print("7. Low Stock Alert") 

    print("8. Generate Bill / Invoice") 

    print("9. Discount Manager") 

    print("10. Exit") 

 

    choice = input("Enter your choice (1-10): ") 

 

    if choice == "1": 

        add_item() 

    elif choice == "2": 

        update_item() 

    elif choice == "3": 

        delete_item() 

    elif choice == "4": 

        view_inventory() 

    elif choice == "5": 

        sell_item() 

    elif choice == "6": 

        daily_sales_report() 

    elif choice == "7": 

        low_stock_alert() 

    elif choice == "8": 

        generate_bill() 

    elif choice == "9": 

        discount_manager() 

    elif choice == "10": 

        print("Thank you for using Valencia Shop Management System! Have a great day!") 

        break 

    else: 

        print("Invalid choice! Please try again.") 
        