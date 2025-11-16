# CSC500 - Principles of Programming - Module 8 Final Portfolio Project
# Michael Spandrio
# 
# Shopping Cart Application - featuring ItemToPurchase and ShoppingCart classes
# Note that this builds and improves upon Modules 4 & 6 Portffolio Milestone submissions
# Attempts were made to center-align menus and outputs to better-align to 
# input requirement example output (albeit at the expense of code readability)
#
# Solution diverges from Modules 4 & 6 solutions in that cart_items is now a dictionary

# ItemToPurchase class with default constructor, initialization within constructor method
class ItemToPurchase:
    DEFAULT_NAME_AND_DESC = "none"
    DEFAULT_PRICE = 0
    DEFAULT_QUANT = 0

    def __init__(self):
        self.item_name = ItemToPurchase.DEFAULT_NAME_AND_DESC
        self.item_description = ItemToPurchase.DEFAULT_NAME_AND_DESC # not part of step 1 reqs, but supports later reqs steps 4,5,6,& 8
        self.item_price = ItemToPurchase.DEFAULT_PRICE
        self.item_quantity = ItemToPurchase.DEFAULT_QUANT

    # Method to print the items cost, multiplying quantity by price
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        item_str = f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f}"
        separator = " = "
        cost_str = f"${total_cost:.2f}"
        print(f"{item_str:>25}{separator}{cost_str:>8}")

# ShoppingCart class with default initialization of customer_name and current_date in default constructor.
class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items: dict[str, ItemToPurchase] = {}

    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, item: ItemToPurchase):
        if item.item_name in self.cart_items:
            print("Item with the same name is already in the cart.".center(60))
            print("Would you like to add the specifed quantity? (y/N):".center(60))
            add_quantity = input((' ' * 20))
            if add_quantity.lower() == 'n':
                print(f"'{item.item_name}' quantity was not updated".center(60))
            else:
                self.cart_items[item.item_name].item_quantity += item.item_quantity
                print(f"'{item.item_name}' quantity was updated to: {self.cart_items[item.item_name].item_quantity}".center(60))
        else:
            self.cart_items[item.item_name] = item

    # Removes item from cart_items list. Has a string (item_name) parameter.
    # If item name cannot be found, output: 'Item not found in cart. Nothing removed.'
    def remove_item(self, item_name: str):
        try:
            del self.cart_items[item_name]
        except KeyError:
            print()
            print("Item not found in cart. Nothing removed.".center(60))                

    # Modifies an item's description, price, and/or quantity.
    # Has parameter ItemToPurchse. Does not return anything.
    # If item can be found (by name) in cart, check if parameter has default
    # values for description, price, and quantity. If not, modify item in cart.
    # If item cannot be found (by name) in cart, output: 'Item not found in cart. Nothing modified.'
    def modify_item(self, item: ItemToPurchase):
        if item.item_name in self.cart_items:
            cart_item = self.cart_items[item.item_name]
            if item.item_description != ItemToPurchase.DEFAULT_NAME_AND_DESC:
                cart_item.item_description = item.item_description
            if item.item_price != ItemToPurchase.DEFAULT_PRICE:
                cart_item.item_price = item.item_price
            if item.item_quantity != ItemToPurchase.DEFAULT_QUANT:
                cart_item.item_quantity = item.item_quantity
        else:
            print()
            print("Item not found in cart. Nothing modified.".center(60))

    # Return quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items.values():
            num_items += item.item_quantity
        return num_items

    # Determines and returns total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        total_cost = 0.00
        for item in self.cart_items.values():
            total_cost += item.item_price * item.item_quantity
        return total_cost

    # Helper method to handle appropriate apostrophe depending on name ending in 's' or not
    def print_cart_heading(self):
        customer_name_suffix = (self.customer_name.endswith('s') and "'") or "'s"
        print(f"{self.customer_name}{customer_name_suffix} Shopping Cart - {self.current_date}".center(60))

    # Output total of objects in cart. If cart is empty, output: 'SHOPPING CART IS EMPTY'
    def print_total(self):
        num_items = self.get_num_items_in_cart()
        print("OUTPUT SHOPPING CART".center(60))
        self.print_cart_heading()
        if num_items == 0:
            print(f"SHOPPING CART IS EMPTY".center(60))
        else:
            print(f"{'Number of Items :':>27}{num_items:>6}")
            for item in self.cart_items.values():
                item.print_item_cost()
            total_str = f"${self.get_cost_of_cart():.2f}"
            separator = " = "
            print(f"{'Total':>25}{separator}{total_str:>8}")

    # Output each items' description
    def print_descriptions(self):
        print(f"OUTPUT ITEMS' DESCRIPTIONS".center(60))
        self.print_cart_heading()
        if self.get_num_items_in_cart() == 0:
            print(f"SHOPPING CART IS EMPTY".center(60))
        else:
            print(f"Item Descriptions".center(60))
            for item in self.cart_items.values():
                desc_name = f"{item.item_name} :"
                print(f"{desc_name:>27}{' ' + item.item_description}")

# Helper method to handle prompt and error handling for price input from user
def get_item_name_input():
    item_name = input((' ' * 7) + "Enter the item name: ")
    # No strict validation requirements. Allow for "free" items at 0 price.
    if not item_name:
        print("Invalid input. Please enter a value for the item name.".center(60))
        return get_item_name_input()
    
    return item_name

# Helper method to handle prompt and error handling for price input from user
def get_item_price_input():
    try:
        item_price = float(input((' ' * 6) + "Enter the item price: "))
        # No strict validation requirements. Allow for "free" items at 0 price.
        if item_price < 0:
            raise ValueError("Price must be non-negative.")
    except ValueError:
        print("Invalid input. Please enter a non-negative numeric value for price.".center(60))
        return get_item_price_input()
    
    return item_price

# Helper method to handle prompt and error handling for quantity input from user
def get_item_quantity_input():
    try:
        item_quantity = int(input((' ' * 3) + "Enter the item quantity: "))
        if item_quantity <= 0:
            raise ValueError("Quantity must be positive.")
    except ValueError:
        print("Invalid input. Please enter a positive integer value for quantity.".center(60))
        return get_item_quantity_input()
    
    return item_quantity

# Has a ShoppingCart parameter an outputs a menu of options to manipulate the shopping cart.
# Each option is represented by a single character. Include error handling for invalid options.
def print_menu(cart: ShoppingCart):
    option = None

    print()
    print("MENU".center(60))
    print(f"{'a - ':>30}Add item to cart")
    print(f"{'r - ':>30}Remove item from cart")
    print(f"{'c - ':>30}Change item quantity")
    print(f"{'i - ':>30}Output items' descriptions")
    print(f"{'o - ':>30}Output shopping cart")
    print(f"{'q - ':>30}Quit")

    while option != 'q':
        print()
        option = input((' ' * 10) + "Choose an option: ")
        print("\n")

        if option == 'q':
            break
        elif option == 'a':
            new_item = ItemToPurchase()
            new_item.item_name = get_item_name_input()
            new_item.item_description = input("Enter the item description: ")
            new_item.item_price = get_item_price_input()
            new_item.item_quantity = get_item_quantity_input()
            cart.add_item(new_item)
        elif option == 'r':
            print("Enter the name of the item to remove: ".center(60))
            item_name = input((' ' * 20))
            cart.remove_item(item_name)
        elif option == 'c':
            # Note that requirement is to allow modification of quantity (even though method supports more)
            item_to_modify = ItemToPurchase()
            item_to_modify.item_name = input("Enter the item name to change quantity in cart: ")
            item_to_modify.item_quantity = get_item_quantity_input()
            cart.modify_item(item_to_modify)
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()
        else:
            print("Invalid option. Please try again.".center(58))

def main():
    print()
    print("Enter customer's name:".center(60))
    customer_name = None
    while True:
        customer_name = input((' ' * 20))

        # Validate: not empty - no strict name input requirements
        if not customer_name:
            print("Invalid entry. Please enter customer's name:".center(60))
        else:
            break

    print("Enter today's date:".center(58))
    current_date = None

    while True:
        current_date = input(' ' * 20)

        # Validate: not empty - no strict date input requirements
        if not current_date:
            print("Invalid entry. Please enter today's date:".center(60))
        else:
            break

    print(f"Customer name: {customer_name}".center(60))
    print(f"Today's date: {current_date}".center(60))

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()