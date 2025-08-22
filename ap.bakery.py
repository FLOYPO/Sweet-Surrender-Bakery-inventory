"""
Enhanced Bakery Inventory System
Author: [Your Name]
Student ID: [Your ID]
Date: [Submission Date]

A comprehensive inventory management system for Sweet Surrender Bakery
with additional features including data persistence and enhanced validation.
"""

import json
import os
from datetime import datetime, timedelta

# Constants
INVENTORY_FILE = "bakery_inventory.json"
DATE_FORMAT = "%Y-%m-%d"

class BakeryInventorySystem:
    """Main inventory system class with enhanced functionality"""
    
    def __init__(self):
        """Initialize the inventory system and load existing data"""
        self.inventory = self.load_inventory()
    
    def load_inventory(self):
        """Load inventory data from JSON file if exists"""
        if os.path.exists(INVENTORY_FILE):
            try:
                with open(INVENTORY_FILE, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Warning: Inventory file corrupted. Starting with empty inventory.")
                return {}
        return {}
    
    def save_inventory(self):
        """Save inventory data to JSON file"""
        try:
            with open(INVENTORY_FILE, 'w') as file:
                json.dump(self.inventory, file, indent=2)
        except IOError:
            print("Error: Could not save inventory data.")
    
    def display_menu(self):
        """Display the main menu and get validated user choice"""
        print("\n" + "="*60)
        print("SWEET SURRENDER BAKERY - ENHANCED INVENTORY SYSTEM")
        print("="*60)
        print("1. Add new ingredient")
        print("2. View all ingredients")
        print("3. Update ingredient quantity")
        print("4. Search ingredient")
        print("5. Remove ingredient")
        print("6. Add expiration date")
        print("7. Check expiring ingredients")
        print("8. Generate inventory report")
        print("9. Exit")
        print("="*60)
        
        while True:
            try:
                choice = int(input("Enter your choice (1-9): ").strip())
                if 1 <= choice <= 9:
                    return choice
                print("Error: Please enter a number between 1 and 9.")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
    
    def add_ingredient(self):
        """Add a new ingredient to the inventory with enhanced validation"""
        print("\n" + "-"*40)
        print("ADD NEW INGREDIENT")
        print("-"*40)
        
        # Get and validate ingredient name
        name = input("Enter ingredient name: ").strip().lower()
        if not name:
            print("Error: Ingredient name cannot be empty.")
            return
        
        if name in self.inventory:
            print(f"Error: '{name}' already exists in inventory.")
            return
        
        # Get and validate quantity
        quantity = input("Enter quantity with unit (e.g., '5 kg', '2 liters'): ").strip()
        if not quantity:
            print("Error: Quantity cannot be empty.")
            return
        
        # Get category
        category = input("Enter category (e.g., 'dry', 'liquid', 'dairy', 'produce'): ").strip().lower()
        
        # Create ingredient entry
        self.inventory[name] = {
            'quantity': quantity,
            'category': category,
            'last_updated': datetime.now().strftime(DATE_FORMAT),
            'expiration_date': None
        }
        
        print(f"Successfully added {quantity} of {name}.")
        self.save_inventory()
    
    def view_inventory(self, sort_by='name'):
        """Display all ingredients with sorting options"""
        print("\n" + "-"*40)
        print("CURRENT INVENTORY")
        print("-"*40)
        
        if not self.inventory:
            print("Inventory is empty. Add some ingredients first!")
            return
        
        # Sort ingredients
        if sort_by == 'name':
            sorted_items = sorted(self.inventory.items())
        elif sort_by == 'category':
            sorted_items = sorted(self.inventory.items(), key=lambda x: x[1].get('category', ''))
        
        print(f"{'Ingredient':<20} {'Quantity':<15} {'Category':<12} {'Expires':<12}")
        print("-" * 60)
        
        for name, data in sorted_items:
            formatted_name = name.capitalize()
            quantity = data.get('quantity', 'N/A')
            category = data.get('category', 'N/A').capitalize()
            exp_date = data.get('expiration_date', 'N/A')
            
            print(f"{formatted_name:<20} {quantity:<15} {category:<12} {exp_date:<12}")
    
    def update_ingredient(self):
        """Update ingredient quantity with enhanced validation"""
        print("\n" + "-"*40)
        print("UPDATE INGREDIENT QUANTITY")
        print("-"*40)
        
        name = input("Enter ingredient name: ").strip().lower()
        if name not in self.inventory:
            print(f"Error: '{name}' not found in inventory.")
            return
        
        current_data = self.inventory[name]
        print(f"Current quantity: {current_data['quantity']}")
        
        try:
            amount = float(input("Enter amount to add (positive) or deduct (negative): ").strip())
        except ValueError:
            print("Error: Invalid amount. Please enter a numeric value.")
            return
        
        # Parse current quantity
        parts = current_data['quantity'].split()
        if len(parts) < 2:
            print("Error: Invalid quantity format in inventory.")
            return
        
        try:
            current_value = float(parts[0])
        except ValueError:
            print("Error: Invalid numeric value in inventory quantity.")
            return
        
        unit = ' '.join(parts[1:])
        new_value = current_value + amount
        
        if new_value < 0:
            print(f"Error: Cannot deduct {abs(amount)} from {current_value} {unit}.")
            return
        
        # Update inventory
        self.inventory[name]['quantity'] = f"{new_value} {unit}"
        self.inventory[name]['last_updated'] = datetime.now().strftime(DATE_FORMAT)
        
        print(f"Updated {name} to {self.inventory[name]['quantity']}")
        self.save_inventory()
    
    def search_ingredient(self):
        """Search for ingredient with partial matching"""
        print("\n" + "-"*40)
        print("SEARCH INGREDIENT")
        print("-"*40)
        
        search_term = input("Enter ingredient name to search: ").strip().lower()
        if not search_term:
            print("Error: Please enter a search term.")
            return
        
        matches = [(name, data) for name, data in self.inventory.items() 
                  if search_term in name]
        
        if not matches:
            print(f"No ingredients found matching '{search_term}'.")
            return
        
        print(f"Found {len(matches)} matching ingredient(s):")
        for name, data in matches:
            print(f"- {name.capitalize()}: {data['quantity']} "
                  f"(Category: {data.get('category', 'N/A')})")
    
    def remove_ingredient(self):
        """Remove an ingredient from inventory"""
        print("\n" + "-"*40)
        print("REMOVE INGREDIENT")
        print("-"*40)
        
        name = input("Enter ingredient name to remove: ").strip().lower()
        if name not in self.inventory:
            print(f"Error: '{name}' not found in inventory.")
            return
        
        confirm = input(f"Are you sure you want to remove {name}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del self.inventory[name]
            print(f"Removed {name} from inventory.")
            self.save_inventory()
        else:
            print("Removal cancelled.")
    
    def add_expiration_date(self):
        """Add or update expiration date for an ingredient"""
        print("\n" + "-"*40)
        print("ADD EXPIRATION DATE")
        print("-"*40)
        
        name = input("Enter ingredient name: ").strip().lower()
        if name not in self.inventory:
            print(f"Error: '{name}' not found in inventory.")
            return
        
        expiration_date = input("Enter expiration date (YYYY-MM-DD) or press Enter to remove: ").strip()
        
        if not expiration_date:
            self.inventory[name]['expiration_date'] = None
            print(f"Removed expiration date for {name}.")
        else:
            try:
                # Validate date format
                datetime.strptime(expiration_date, DATE_FORMAT)
                self.inventory[name]['expiration_date'] = expiration_date
                print(f"Set expiration date for {name} to {expiration_date}.")
            except ValueError:
                print("Error: Invalid date format. Please use YYYY-MM-DD.")
                return
        
        self.save_inventory()
    
    def check_expiring_ingredients(self, days=7):
        """Check for ingredients expiring within specified days"""
        print("\n" + "-"*40)
        print("EXPIRING INGREDIENTS CHECK")
        print("-"*40)
        
        today = datetime.now()
        expiring_ingredients = []
        
        for name, data in self.inventory.items():
            exp_date_str = data.get('expiration_date')
            if exp_date_str:
                try:
                    exp_date = datetime.strptime(exp_date_str, DATE_FORMAT)
                    if 0 <= (exp_date - today).days <= days:
                        expiring_ingredients.append((name, data, (exp_date - today).days))
                except ValueError:
                    continue
        
        if not expiring_ingredients:
            print(f"No ingredients expiring within the next {days} days.")
            return
        
        print(f"Ingredients expiring within the next {days} days:")
        for name, data, days_until in expiring_ingredients:
            print(f"- {name.capitalize()}: {data['quantity']} "
                  f"(Expires in {days_until} days on {data['expiration_date']})")
    
    def generate_report(self):
        """Generate a comprehensive inventory report"""
        print("\n" + "-"*40)
        print("INVENTORY REPORT")
        print("-"*40)
        
        total_items = len(self.inventory)
        categories = {}
        expiring_soon = 0
        
        for data in self.inventory.values():
            category = data.get('category', 'uncategorized')
            categories[category] = categories.get(category, 0) + 1
            
            # Check for ingredients expiring within 3 days
            exp_date_str = data.get('expiration_date')
            if exp_date_str:
                try:
                    exp_date = datetime.strptime(exp_date_str, DATE_FORMAT)
                    if (exp_date - datetime.now()).days <= 3:
                        expiring_soon += 1
                except ValueError:
                    continue
        
        print(f"Total ingredients: {total_items}")
        print(f"Categories: {', '.join([f'{k.capitalize()}: {v}' for k, v in categories.items()])}")
        print(f"Ingredients expiring within 3 days: {expiring_soon}")
        print(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def run(self):
        """Main program execution loop"""
        print("="*70)
        print("WELCOME TO SWEET SURRENDER BAKERY ENHANCED INVENTORY SYSTEM")
        print("="*70)
        
        try:
            while True:
                choice = self.display_menu()
                
                if choice == 1:
                    self.add_ingredient()
                elif choice == 2:
                    self.view_inventory()
                elif choice == 3:
                    self.update_ingredient()
                elif choice == 4:
                    self.search_ingredient()
                elif choice == 5:
                    self.remove_ingredient()
                elif choice == 6:
                    self.add_expiration_date()
                elif choice == 7:
                    try:
                        days = int(input("Check ingredients expiring within how many days? (default 7): ") or 7)
                        self.check_expiring_ingredients(days)
                    except ValueError:
                        print("Error: Please enter a valid number of days.")
                elif choice == 8:
                    self.generate_report()
                elif choice == 9:
                    print("\nThank you for using the Enhanced Bakery Inventory System!")
                    print("Exiting the program. Goodbye!")
                    break
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting gracefully.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again or contact support if the problem persists.")

# Run the enhanced system
if __name__ == "__main__":
    system = BakeryInventorySystem()
    system.run()