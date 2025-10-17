# CSC500 - Principles of Programming - Module 3 Critical Thinking Part 1
# Michael Spandrio
# 
# Calculate tax, tip and total from the cost of a meal at a restaurant
import sys

def main():
    # constants
    tax_pct = 0.07
    tip_pct = 0.18

    meal_cost = None
    # error handling (int or float input is accepted & converted to float, error otherwise)
    try:
        meal_cost = float(input("\nEnter the meal cost: "))
        if meal_cost <= 0:
            raise ValueError("Input number must be positive.")
    except ValueError:
        print("\nInvalid input. Please enter a positive numeric value.\n")
        sys.exit(1)

    # added_tip calculated based on pre-tax meal cost
    added_tip = meal_cost * tip_pct

    # tax based on the meal cost without tip
    tax = meal_cost * tax_pct

    print("\nMeal cost:  ${:.2f}".format(meal_cost))
    print("Tax  (7%):   ${:.2f}".format(tax))
    print("Tip (18%):   ${:.2f}".format(added_tip))
    print("Total cost: ${:.2f}\n".format(meal_cost + tax + added_tip))

if __name__ == "__main__":
    main()