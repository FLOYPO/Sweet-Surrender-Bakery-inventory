# Sweet Surrender Bakery Inventory System
# Developed for managing ingredients using a simple dictionary structure

# Dictionary to store ingredient data
inventory = {}

# Function to add a new ingredient
def add_ingredient():
    name = input("Enter the ingredient name: ").lower()
    if name in inventory:
        print(f"{name.title()} already exists in the inventory.")
    else:
        try:
            amount = float(input(f"Enter the quantity of {name}: "))
            unit = input("Enter the unit (e.g., kilos, litres): ").lower()
            inventory[name] = {"amount": amount, "unit": unit}
            print(f"{name.title()} added successfully.")
        except ValueError:
            print("Invalid input. Quantity must be a number.")

# Function to view all ingredients
def view_inventory():
    if not inventory:
        print("Inventory is currently empty.")
    else:
        print("\nCurrent Inventory:")
        for ingredient, details in inventory.items():
            print(f"- {ingredient.title()}: {details['amount']} {details['unit']}")
        print()

# Function to update the quantity of an existing ingredient
def update_ingredient():
    name = input("Enter the ingredient to update: ").lower()
    if name in inventory:
        try:
            used = float(input(f"Enter amount of {name} used: "))
            if used < 0:
                print("Usage must be a positive number.")
                return
            if used > inventory[name]["amount"]:
                print(f"Not enough {name}. Only {inventory[name]['amount']} {inventory[name]['unit']} available.")
            else:
                inventory[name]["amount"] -= used
                print(f"{name.title()} updated. Remaining: {inventory[name]['amount']} {inventory[name]['unit']}")
        except ValueError:
            print("Invalid input. Quantity must be a number.")
    else:
        print(f"{name.title()} not found in inventory.")

# Function to search for a specific ingredient
def search_ingredient():
    name = input("Enter the ingredient to search for: ").lower()
    if name in inventory:
        print(f"{name.title()} - {inventory[name]['amount']} {inventory[name]['unit']}")
    else:
        print(f"{name.title()} not found in inventory.")

# Function to delete an ingredient from the inventory
def delete_ingredient():
    name = input("Enter the ingredient name to delete: ").lower()
    if name in inventory:
        del inventory[name]
        print(f"{name.title()} deleted successfully!")
    else:
        print(f"Error: {name.title()} is not in the system.")

# Function to display menu
def display_menu():
    print("\n--- Sweet Surrender Bakery Inventory Menu ---")
    print("1. Add New Ingredient")
    print("2. View All Ingredients")
    print("3. Update Ingredient Quantity")
    print("4. Search Ingredient")
    print("5. Delete Ingredient")
    print("6. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_ingredient()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_ingredient()
        elif choice == '4':
            search_ingredient()
        elif choice == '5':
            delete_ingredient()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")

# Run the program
if __name__ == "__main__":
    main()
