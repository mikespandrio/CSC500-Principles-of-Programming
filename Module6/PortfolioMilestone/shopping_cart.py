# CSC500 - Principles of Programming - Module 6 Portfolio Milestone
# Michael Spandrio
# 
# Build the ShoppingCart class
# Note that this builds and improves upon Module 4's Portffolio Milestone submission

class ItemToPurchase:
    DEFAULT_NAME_AND_DESC = "none"
    DEFAULT_PRICE = 0.00
    DEFAULT_QUANT = 0

    def __init__(self):
        self.item_name = ItemToPurchase.DEFAULT_NAME_AND_DESC
        self.item_description = ItemToPurchase.DEFAULT_NAME_AND_DESC
        self.item_price = ItemToPurchase.DEFAULT_PRICE
        self.item_quantity = ItemToPurchase.DEFAULT_QUANT

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # helper method for add, remove, and modify to avoid repetitive code (DRY)
    def find_item_index(self, item_name):
        i = 0
        while i < len(self.cart_items):
            cart_item = self.cart_items[i]
            if cart_item.item_name == item_name:
                return i
            i += 1
        return -1

    def add_item(self, item: ItemToPurchase):
        if self.find_item_index(item.item_name) >= 0:
            print("Item with the same name is already in the cart. A duplicate item was not added.")
            return
        # only if item not found, add it
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        item_index = self.find_item_index(item_name)
        if item_index >= 0:
            del self.cart_items[item_index]
        else:
            print("\nItem not found in cart. Nothing removed.")        

    def modify_item(self, item: ItemToPurchase):
        item_index = self.find_item_index(item.item_name)
        if item_index >= 0:
            cart_item = self.cart_items[item_index]
            if item.item_description != ItemToPurchase.DEFAULT_NAME_AND_DESC:
                cart_item.item_description = item.item_description
            if item.item_price != ItemToPurchase.DEFAULT_PRICE:
                cart_item.item_price = item.item_price
            if item.item_quantity != ItemToPurchase.DEFAULT_QUANT:
                cart_item.item_quantity = item.item_quantity
        else:
            print("\nItem not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0.00
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_cart_heading(self):
        customer_name_suffix = (self.customer_name.endswith('s') and "'") or "'s"
        print(f"{self.customer_name}{customer_name_suffix} Shopping Cart - {self.current_date}")

    def print_total(self):
        num_items = self.get_num_items_in_cart()
        print("OUTPUT SHOPPING CART")
        self.print_cart_heading()
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {num_items}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        self.print_cart_heading()
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Item Descriptions")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}")

def get_item_price_input():
    try:
        item_price = float(input("Enter the item price: "))
        if item_price < 0:
            raise ValueError("Price must be non-negative.")
    except ValueError:
        print("Invalid input. Please enter a non-negative numeric value for price.")
        return get_item_price_input()
    
    return item_price

def get_item_quantity_input():
    try:
        item_quantity = int(input("Enter the item quantity: "))
        if item_quantity <= 0:
            raise ValueError("Quantity must be positive.")
    except ValueError:
        print("Invalid input. Please enter a positive integer value for quantity.")
        return get_item_quantity_input()
    
    return item_quantity


def print_menu(cart: ShoppingCart):
    option = None

    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

    while option != 'q':
        option = input("\nChoose an option: ")
        print()

        if option == 'q':
            break
        elif option == 'a':
            new_item = ItemToPurchase()
            new_item.item_name = input("Enter the item name: ")
            new_item.item_description = input("Enter the item description: ")
            new_item.item_price = get_item_price_input()
            new_item.item_quantity = get_item_quantity_input()
            cart.add_item(new_item)
        elif option == 'r':
            item_name = input("Enter the name of the item to remove: ")
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
            print("Invalid option. Please try again.")

def main():
    john_doe_cart = ShoppingCart("John Doe", "February 1, 2020")
    print_menu(john_doe_cart)

if __name__ == "__main__":
    main()