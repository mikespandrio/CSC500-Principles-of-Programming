# CSC500 - Principles of Programming - Module 4 Portfolio Milestone
# Michael Spandrio
# 
# Build the ItemToPurchase class

class ItemToPurchase:

    # Note on requirements: Default Constructor below w/ no parameters,
    #  but by providing parameters with defaults could be another approach,
    #  such as __init(self, item_name="none", item_price=0, item_quantity=0):
    #  then setting self.<param> = <param>
    #  Requirements were taken literally to mean "default constructor w/ no parameters"
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price, total_cost))

# function to create an item with user input and error handling
def create_item():
    item = ItemToPurchase()
    item.item_name = input("Enter the item name:\n")

    try:
        item_price = float(input("Enter the item price:\n"))
        if (item_price < 0):
            raise ValueError("Price must be non-negative.")
        item.item_price = item_price
    except ValueError:
        print("Invalid input. Please enter a non-negative numeric value for price.")
        exit(1)

    try:
        item_quantity = int(input("Enter the item quantity:\n"))
        if (item_quantity < 0):
            raise ValueError("Quantity must be non-negative.")
        item.item_quantity = item_quantity
    except ValueError:
        print("Invalid input. Please enter a non-negative integer value for quantity.")
        exit(1)

    return item

def main():
    print("Item 1")
    item1 = create_item()

    print("\nItem 2")
    item2 = create_item()

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print("Total: ${:.2f}\n".format((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)))

if __name__ == "__main__":
    main()
