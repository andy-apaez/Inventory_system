import json

# File to store inventory
INVENTORY_FILE = "inventory.json"

# Load inventory
def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save inventory to file
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

# Show inventory
def view_inventory(inventory):
    if not inventory:
        print("📦 Inventory is empty.")
    else:
        print("\n--- Current Inventory ---")
        for item, details in inventory.items():
            print(f"{item}: {details['quantity']} units @ ${details['price']} each")
        print("-------------------------\n")

# Add new item
def add_item(inventory):
    item = input("Enter item name: ").capitalize()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory[item] = {"quantity": quantity, "price": price}
    print(f"✅ Added {item} to inventory.")

# Update item quantity
def update_item(inventory):
    item = input("Enter item name to update: ").capitalize()
    if item in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[item]["quantity"] = quantity
        print(f"🔄 Updated {item} quantity to {quantity}.")
    else:
        print("❌ Item not found.")

# Remove item
def remove_item(inventory):
    item = input("Enter item name to remove: ").capitalize()
    if item in inventory:
        del inventory[item]
        print(f"🗑️ Removed {item} from inventory.")
    else:
        print("❌ Item not found.")

# Main program
# fix the while true (bad format)
def main():
    inventory = load_inventory()

    while True:
        print("\n📋 Inventory Menu")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Save & Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("💾 Inventory saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
