from core import validate_inputs, inventory_register

inventorylist = []
def main(customers_db, products_db, orders_db, order_id):
    
    #This is the introduction message
    print("--- Inventory System ---")

    #We run the program In a while loop, so the program only stop when we decide.  
    option = ":)"
    while option != 0 :
        #This is the menu options.
        print("\n1. Register Product \n2. View Inventory \n3. Calculate Statistics \n4. View Orders\n5. Daily Income\n6. Final Report & Exit")
        option = input("Select an option: ")
        
        if option == "1":
            #The first option is to create a new user in the user database.
            product_name_validated = validate_inputs(str, "name product")
            price_validated = validate_inputs(float,"price",True)
            quantity_validated = validate_inputs(int,"quantity",True)
            
            inventory_register(product_name_validated,quantity_validated,price_validated,inventorylist)
          
            print("Customer registered.")
            
        elif option == "2":
            #This is the option to create a new product in the product database.
            
            
            print("Product registered.")