# Historia_de_usuario_M1S2
# Inventory Management System

A Python-based inventory management tool designed for product registration, view the inventory and calculate some statistics.

## Description
This program captures product data including name, price, and quantity. It features input validation to prevent runtime errors and ensure data integrity, also the system generates a detailed summary and calculates basic statistics about the data.

## Features
* **Data Validation:** Implements `validate_inputs` blocks to ensure prices are processed as floats and quantities as integers.
* **Modular Design:** Separation of concerns between the entry point (`main.py`) and business logic (`core.py`).
* **Dynamic Management:** Utilizes lists and dictionaries to handle multiple records within a single execution session.

## Project Structure
* `main.py`: The main entry point containing the user interaction loop.
* `core.py`: External module containing the `validate_inputs`,`inventory_register` and `show_summary` functions.
* `README.md`: Technical documentation of the project.

## Requirements
* Python 3.x.
* Ensure `core.py` is located in the same directory as the main execution file.

## Usage Instructions
1. Run the application from the terminal: `python main.py`.
2. Enter the option in the menu.
3. If option is 1 provide the name, unit price and quantity; the system will reject negative values or non-numeric inputs.
4. If option is 2 view the summary of the products registered
5. If option is 3 view the statistics of the inventory
6. Exit the program with option 0

## Example Execution
```text
--- Inventory System ---

1. Register Product 
2. View Inventory 
3. Calculate Statistics 
0. Exit
Select an option: 1
Enter name product: Azucar
Enter price: 100
Enter quantity: 3
Product Azucar successfully registered!

1. Register Product 
2. View Inventory 
3. Calculate Statistics 
0. Exit
Select an option: 3
The total number of products registered was 1, 3 units were stored, and the total inventory value is 300.0

1. Register Product 
2. View Inventory 
3. Calculate Statistics 
0. Exit
Select an option: 2
Azucar 
Quantity of product in the inventory: 3 
Price per unit: $100.0
Total value of the product in inventory: $300.0
--------------------
```
