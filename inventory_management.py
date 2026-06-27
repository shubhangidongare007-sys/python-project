import os

# Global dictionary as requested on Page 17
inventory = {}

# 1. load_inventory() - Read data from inventory.txt
def load_inventory():
    global inventory
    if os.path.exists("inventory.txt"):
        try:
            with open("inventory.txt", "r") as f:
                for line in f:
                    if line.strip():
                        p_id, name, cat, price, qty, reorder = line.strip().split(",")
                        inventory[p_id] = {
                            "name": name,
                            "category": cat,
                            "price": float(price),
                            "quantity": int(qty),
                            "reorder_level": int(reorder)
                        }
            print(f"Products Loaded: {len(inventory)}")
        except:
            print("Error loading file. Starting fresh.")
    else:
        # Pre-populate with 8 products across 3 categories (Rule 14 on Page 18)
        inventory = {
            "P001": {"name": "Laptop", "category": "Electronics", "price": 45000.0, "quantity": 12, "reorder_level": 3},
            "P002": {"name": "Mouse", "category": "Electronics", "price": 600.0, "quantity": 25, "reorder_level": 5},
            "P003": {"name": "Keyboard", "category": "Electronics", "price": 1200.0, "quantity": 4, "reorder_level": 5},
            "P004": {"name": "Notebook", "category": "Stationery", "price": 60.0, "quantity": 50, "reorder_level": 10},
            "P005": {"name": "Pen", "category": "Stationery", "price": 20.0, "quantity": 100, "reorder_level": 20},
            "P006": {"name": "Shirt", "category": "Apparel", "price": 999.0, "quantity": 15, "reorder_level": 4},
            "P007": {"name": "Jeans", "category": "Apparel", "price": 1499.0, "quantity": 2, "reorder_level": 5},
            "P008": {"name": "Marker", "category": "Stationery", "price": 30.0, "quantity": 8, "reorder_level": 10}
        }
        save_inventory()

# 2. save_inventory() - Write data to inventory.txt
def save_inventory():
    try:
        with open("inventory.txt", "w") as f:
            for p_id, data in inventory.items():
                f.write(f"{p_id},{data['name']},{data['category']},{data['price']},{data['quantity']},{data['reorder_level']}\n")
    except:
        print("Error saving data.")

# 3. add_product() - Register new product
def add_product():
    print("\n--- Add Product ---")
    p_id = input("Enter Product ID: ").strip().upper()
    if p_id in inventory:
        print("Error: Unique Product ID enforcement! ID already exists.")
        return

    name = input("Enter Product Name: ").strip()
    category = input("Enter Category: ").strip()
    
    try:
        price = float(input("Enter Unit Price: "))
        qty = int(input("Enter Quantity: "))
        reorder = int(input("Enter Reorder Level: "))
        
        if price < 0 or qty < 0 or reorder < 0:
            print("Error: Numbers cannot be negative!")
            return
    except ValueError:
        print("Error: Invalid number input!")
        return

    inventory[p_id] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": qty,
        "reorder_level": reorder
    }
    print("Product added successfully.")

# 4. stock_in() - Add quantity
def stock_in():
    print("\n--- Stock In ---")
    p_id = input("Enter Product ID: ").strip().upper()
    if p_id not in inventory:
        print("Error: Product ID not found.")
        return
    try:
        qty = int(input("Enter Quantity to Add: "))
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Invalid number.")
        return

    inventory[p_id]["quantity"] += qty
    print("Stock updated.")
    save_inventory()

# 5. stock_out() - Deduct quantity with validation
def stock_out():
    print("\n--- Stock Out ---")
    p_id = input("Enter Product ID: ").strip().upper()
    if p_id not in inventory:
        print("Error: Product ID not found.")
        return
    try:
        qty = int(input("Enter Quantity to Deduct: "))
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Invalid number.")
        return

    # Stock level validation before stock-out (Page 17 Rule 11)
    if inventory[p_id]["quantity"] < qty:
        print(f"Error: Insufficient stock! Available: {inventory[p_id]['quantity']}.")
        return

    inventory[p_id]["quantity"] -= qty
    print("Stock deducted.")
    
    # Automatic low stock detection
    if inventory[p_id]["quantity"] <= inventory[p_id]["reorder_level"]:
        print(f"⚠️ ALERT: {inventory[p_id]['name']} is below reorder level!")

# 6. view_inventory() - Display full formatted table
def view_inventory():
    print("\n" + "="*65)
    print(f"{'ID':<8} {'Name':<15} {'Category':<15} {'Price':<10} {'Qty':<8}")
    print("="*65)
    for p_id, d in inventory.items():
        print(f"{p_id:<8} {d['name']:<15} {d['category']:<15} {d['price']:<10.2f} {d['quantity']:<8}")
    print("="*65)

# 7. low_stock_alert() - List products below reorder level
def low_stock_alert():
    print("\n--- Low Stock Items ---")
    found = False
    for p_id, d in inventory.items():
        if d["quantity"] <= d["reorder_level"]:
            print(f"⚠️ ID: {p_id} | {d['name']} | Stock: {d['quantity']} (Limit: {d['reorder_level']})")
            found = True
    if not found:
        print("All items are fully stocked.")

# 8. generate_report() - Summary statistics
def generate_report():
    print("\n====== INVENTORY REPORT ======")
    print(f"Total Products : {len(inventory)}")
    
    total_value = sum(d["price"] * d["quantity"] for d in inventory.values())
    print(f"Total Stock Value : Rs. {total_value:.2f}")
    
    # Category list using Sets
    categories = {d["category"] for d in inventory.values()}
    print(f"Categories : {', '.join(categories)}")
    print("==============================")

# 8. Flow of Execution (Main Loop)
def main():
    load_inventory()
    while True:
        print("\n----- MENU -----")
        print("1. Add Product")
        print("2. Stock In")
        print("3. Stock Out")
        print("4. View Inventory")
        print("5. Low Stock Alert")
        print("6. Report")
        print("7. Save & Exit")
        
        choice = input("Choice: ").strip()
        if choice == "1": add_product()
        elif choice == "2": stock_in()
        elif choice == "3": stock_out()
        elif choice == "4": view_inventory()
        elif choice == "5": low_stock_alert()
        elif choice == "6": generate_report()
        elif choice == "7":
            save_inventory()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()