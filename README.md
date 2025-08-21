This is a simple console-based inventory management system developed in Python for Sweet Surrender Bakery. The system allows the bakery to keep track of its ingredients using a dictionary structure. It provides a straightforward way to add, view, update, search for, and delete ingredients.

Features
Add New Ingredient: Add a new ingredient to the inventory with its quantity and unit of measurement.

View All Ingredients: Display a complete list of all ingredients currently in stock.

Update Quantity: Reduce the quantity of an existing ingredient after it's been used in baking.

Search for Ingredient: Quickly check the stock of a specific ingredient.

Delete Ingredient: Remove an ingredient from the inventory.

How to Use
Prerequisites
Make sure you have Python 3 installed on your computer.

Running the Program
Save the code in a file named inventory_system.py.

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the program using the following command:

Bash

python inventory_system.py

Menu Options
Once the program is running, you'll see a menu with six options. Simply enter the number corresponding to the action you want to perform and press Enter.

1. Add New Ingredient: You will be prompted to enter the ingredient's name, quantity, and unit.

2. View All Ingredients: This will display a list of all ingredients and their current stock levels.

3. Update Ingredient Quantity: Enter the name of the ingredient you want to update, then enter the amount used. The system will automatically calculate the new remaining quantity.

4. Search Ingredient: Enter the name of the ingredient you want to find to see its current stock.

5. Delete Ingredient: Enter the name of the ingredient you wish to remove from the system.

6. Exit: This will close the program.

Code Structure
The program is organized into several functions to make the code clean and easy to understand.

inventory = {}: A global dictionary that acts as the central database for all ingredients.

add_ingredient(): Handles the logic for adding a new item to the inventory dictionary. It includes error handling to ensure the quantity is a valid number.

view_inventory(): Iterates through the inventory dictionary and prints all ingredients and their details.

update_ingredient(): Allows for a specified quantity to be subtracted from an existing ingredient's stock. It checks for sufficient stock and validates input.

search_ingredient(): Looks up an ingredient by name and prints its details if found.

delete_ingredient(): Removes an ingredient from the inventory dictionary.

display_menu(): Presents the main menu to the user.

main(): The primary function that runs the program. It contains a while True loop to keep the program running until the user chooses to exit.
