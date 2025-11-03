# Pharmacy Inventory Manager v1.0
# Track drug stock, add/remove inventory, get low stock alerts

from datetime import datetime

# Initialize empty inventory
inventory = {}

def add_drug():
    """Add new drug or increase existing stock"""
    print("\n--- ADD DRUG TO INVENTORY ---")
    
    # Get drug name
    drug_name = input("Drug name: ").strip().lower()
    if not drug_name:
        print("❌ Drug name cannot be empty")
        return
    
    # Get quantity to add
    try:
        quantity = int(input("Quantity to add: ").strip())
        if quantity <= 0:
            print("❌ Quantity must be positive")
            return
    except ValueError:
        print("❌ Invalid quantity. Please enter a number.")
        return
    
    # Add to inventory
    if drug_name in inventory:
        inventory[drug_name] += quantity
        print(f"✅ Added {quantity} units of {drug_name.title()}")
        print(f"   New stock level: {inventory[drug_name]} units")
    else: 
        inventory[drug_name] = quantity
        print(f"✅ New drug added: {drug_name.title()} - {quantity} units")

def remove_drug():
    """Remove/decrease drug stock"""
    print("\n--- REMOVE DRUG FROM INVENTORY ---")

    if not inventory:
        print("❌ Inventory is empty. Nothing to remove.")
        return
    
    # Get drug name
    drug_name = input("Drug name: ").strip().lower()

    if drug_name not in inventory:
        print(f"❌ {drug_name.title()} not found in inventory")
        return
    
    # Get quantity to remove
    try:
        quantity = int(input("Quantity to remove: ").strip())
        if quantity <= 0:
            print("❌ Quantity must be positive")
            return
    except ValueError:
        print("❌ Invalid quantity. Please enter a number.")
        return
    
    # Remove from inventory
    if quantity > inventory[drug_name]:
        print(f"❌ Cannot remove {quantity} units. Only {inventory[drug_name]} available.")
        return
    
    inventory[drug_name] -= quantity

    if inventory[drug_name] == 0:
        del inventory[drug_name]
        print(f"✅ Removed all {drug_name.title()} from inventory")
    else:
        print(f"✅ Removed {quantity} units of {drug_name.title()}")
        print(f"   Remaining stock: {inventory[drug_name]} units")


def view_inventory():
    """Display all drugs and quantities"""
    print("\n" + "=" * 60)
    print("     CURRENT INVENTORY")
    print("=" * 60)

    if not inventory:
        print("📦 Inventory is empty")
        return
    
    print(f"\nTotal drugs in stock: {len(inventory)}")
    print("\n{:<30} {:>10}".format("Drug name", "Quantity"))
    print("-" * 60)

    for drug_name in sorted(inventory.keys()):
        quantity = inventory[drug_name]
        print(f"{drug_name.title():<30} {quantity:>10} units")

    print("=" * 60)


def check_low_stock():
    """Alert for new drugs below threshold"""
    print("\n--- LOW STOCK ALERTS ---")

    if not inventory:
        print("📦 Inventory is empty")
        return
    
    try:
        threshold = int(input("Enter low stock threshold: ").strip())
        if threshold < 0:
            print("❌ Threshold must be positive")
            return
    except ValueError:
        print("❌ Invalid threshold")
        return
    
    low_stock_drugs = {drug: qty for drug, qty in inventory.items() if qty <= threshold}

    if not low_stock_drugs:
        print(f"✅ No drugs below {threshold} units")
        return

    print(f"\n⚠️   {len(low_stock_drugs)} drug(s) below {threshold} units:")
    print("\n{:<30} {:>10}".format("Drug name", "Quantity"))
    print("-" * 60)

    for drug_name in sorted(low_stock_drugs.keys()):
        quantity = low_stock_drugs[drug_name]
        print(f"{drug_name.title():<30} {quantity:>10} units")

def save_inventory():
    """Export inventory to file"""
    if not inventory:
        print("❌ Inventory is empty. Nothing to save.")
        return
    
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"inventory.{today}.txt"

    try:
        with open(filename, "w") as f:
            f.write("=" * 60 + "\n")
            f.write("     PHARMACY INVENTORY REPORT\n")
            f.write("=" * 60 + "\n")
            f.write(f"Date: {today}\n")
            f.write(f"Total drugs in stock: {len(inventory)}\n\n")

            f.write(f"{'Drug Name':<30} {'Quantity':>10}\n")
            f.write("=" * 60 + "\n")

            for drug_name in sorted(inventory.keys()):
                quantity = inventory[drug_name]
                f.write(f"{drug_name.title():<30} {quantity:>10} units\n")

            f.write("=" * 60 + "\n")

        print(f"✅ Inventory saved to: {filename}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

# Main program loop
def main(): 
    print("=" * 60)
    print("     PHARMACY INVENTORY MANAGER v1.0")
    print("=" * 60)

    while True:
        print("\n--- MENU ---")
        print("1. Add drug to inventory")
        print("2. Remove drug from inventory")
        print("3. View current inventory")
        print("4. Check low stock alerts")
        print("5. Export inventory to file")
        print("6. Exit")

        choice = input("\nSelect option (1-6): ").strip()

        if choice == "1":
            add_drug()
        elif choice == "2":
            remove_drug()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            check_low_stock()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            print("\n✅ Inventory manager closed. See you next time playa!")
            break
        else: 
            print("❌ Invalid option. Please select 1-6.")

if __name__ == "__main__":
    main()


