# CSC500-Principles-of-Programming
Course Assignments - Part of CSU Global Master's in AI &amp; ML Program

[Module 1: Critical Thinking Assignment](#module-1-critical-thinking-assignment)  
[Module 3: Critical Thinking Assignment](#module-3-critical-thinking-assignment)  
[Module 4: Portfolio Milestone Assignment](#module-4-portfolio-milestone)  
[Module 5: Critical Thinking Assignment](#module-5-critical-thinking-assignment)  
[Module 6: Portfolio Milestone Assignment](#module-6-portfolio-milestone)  

# Module 1: Critical Thinking Assignment

## Overview
The assignment is divided into two parts: 
Part 1 focuses on addition and subtraction
Part 2 focuses on multiplication and division.  

All files for this assignment are organized within the following directory:  
`/Module1/CriticalThinking` 

---

## Part 1: Addition and Subtraction
**Objective:** Write a Python program that asks the user to input two numbers (`num1` and `num2`).  
The program should add the two numbers to find the sum and subtract them to find the difference.

**Files Included:**
- `add_and_subtract.py` — Python source file for Part 1  

**Pseudocode:**

***Begin***

1. Display message: *"This program will output the sum and difference of the two user-entered numbers."*

2. Prompt user to **enter the first integer value**  
   - If input is not an integer, display error: *"Incorrect input format. Please enter an integer value."*  
   - Exit program.

3. Prompt user to **enter the second integer value**  
   - If input is not an integer, display error: *"Incorrect input format. Please enter an integer value."*  
   - Exit program.

4. Compute **sum_of_nums = num1 + num2**

5. Compute **diff_of_nums = num1 - num2**

6. Display header: *"RESULTS:"*

7. Display the sum in a formatted message:  
   *"The sum of [num1] and [num2] is: [sum_of_nums]"*

8. Display the difference in a formatted message:  
   *"The difference between [num1] and [num2] is: [diff_of_nums]"*

***End***


---

## Part 2: Multiplication and Division
**Objective:** Write a Python program that asks the user to input two numbers (`num1` and `num2`).  
The program should multiply the two numbers to find the product and divide `num1` by `num2` to find the quotient.

**Files Included:**
- `multiply_and_divide.py` — Python source file for Part 2  

**Pseudocode:**

***Begin***

1. Display message: *"This program will output the product and quotient of the two user-entered numbers."*

2. Prompt user to **enter the first integer value**  
   - If input is not an integer, display error: *"Incorrect input format. Please enter an integer value."*  
   - Exit program.

3. Prompt user to **enter the second integer value**  
   - If input is not an integer, display error: *"Incorrect input format. Please enter an integer value."*  
   - Exit program.

4. Compute **product_of_nums = num1 × num2**

5. Display header: *"RESULTS:"*

6. Display the product in a formatted message:  
   *"The product of [num1] and [num2] is: [product_of_nums]"*

7. Attempt to compute **quotient_of_nums = num1 ÷ num2**
   - If **num2 = 0**, display error: *"Cannot divide by zero, please re-run program and choose a different second number."*  
   - Exit program.

8. If no error occurs, display the quotient in a formatted message:  
   *"The quotient of [num1] and [num2] is: [quotient_of_nums]"*

***End***

---

# Module 3: Critical Thinking Assignment

## Overview
The assignment is divided into two parts:  
Part 1 focuses on calculating restaurant meal costs, including tip, tax, and total amount due.  
Part 2 focuses on using modular arithmetic to determine future time on a 24-hour clock based on user input.

All files for this assignment are organized within the following directory:  
`/Module3/CriticalThinking` 

---

## Part 1: Calculate Meal Cost
**Objective:** Write a Python program that calculates the total cost of a restaurant meal, including tax and tip, based on the user’s input for the meal charge.  
The program should request the meal cost from the user, calculate an 18% tip and a 7% sales tax, then display each amount and the total price.

**Files Included:**
- `meal_tax_and_tip.py` — Python source file for Part 1  

**Pseudocode:**

***Begin***

1. Display message: *"This program calculates the tax, tip, and total from the cost of a meal at a restaurant."*

2. Define constants for:
   - **tax_pct = 0.07**
   - **tip_pct = 0.18**

3. Prompt user to **enter the meal cost**
   - Convert input to a floating-point number.  
   - If the input is not numeric or less than or equal to zero, display error:  
     *"Invalid input. Please enter a positive numeric value."*  
   - Exit program.

4. Compute **added_tip = meal_cost × tip_pct**

5. Compute **tax = meal_cost × tax_pct**

6. Compute **total = meal_cost + added_tip + tax**

7. Display formatted results:
   - *"Meal cost:  $[meal_cost]"*
   - *"Tax (7%):   $[tax]"*
   - *"Tip (18%):  $[added_tip]"*
   - *"Total cost: $[total]"*

***End***

---

## Part 2: 24-hour Alarm Clock
**Objective:** Write a Python program that determines the future time on a 24-hour clock when an alarm will go off.  
The program should ask the user for the current time (in hours, using the 24-hour format) and for the number of hours to wait. It should then calculate and display the hour when the alarm will sound, wrapping around if the time exceeds 24 hours.

**Files Included:**
- `set_alarm.py` — Python source file for Part 2  

**Pseudocode:**

***Begin***

1. Display message: *"This program calculates the time your alarm will sound based on the current hour (on a 24-hour clock) and hours to wait"*

2. Prompt user to **enter the current hour (24-hour clock)**  
   - Convert input to an integer.  
   - If the value is not between 0 and 23 (inclusive), display error:  
     *"Invalid input. Please enter an integer value between 0 and 23 (inclusive)."*  
   - Exit program.

3. Prompt user to **enter the number of hours to wait until the alarm sounds**  
   - Convert input to an integer.  
   - If the value is not positive, display error:  
     *"Invalid input. Please enter a positive integer value."*  
   - Exit program.

4. Compute **alarm_hour = (time_in_hours + hours_to_wait) % 24**

5. Display the result in formatted output:  
   *"The alarm will sound at [alarm_hour]:00 (based on 24-hour clock)."*

***End***

---

# Module 4: Portfolio Milestone

## Overview
This milestone introduces class-based programming concepts through the design and implementation of an object-oriented shopping cart system.  
The task involves defining a class to represent purchasable items, instantiating objects from user input, and computing their total cost.  

All files for this assignment are organized within the following directory:  
`/Module4/PortfolioMilestone`

---

## Online Shopping Cart

**Objective:**  
Write a Python program that models a basic online shopping cart using an `ItemToPurchase` class.  
The class should contain item details (name, price, and quantity) and a method to print the item’s cost.  
The main program should create two items based on user input and display individual and total costs.

**Files Included:**  
- `item_to_purchase.py` — Python source file for this milestone  

**Pseudocode:**

***Begin***

### Step 1: Define the ItemToPurchase class
1. Create class **ItemToPurchase** with the following **attributes**:  
   - `item_name` (string)  
   - `item_price` (float)  
   - `item_quantity` (int)  
2. Define a **default constructor** to initialize:  
   - `item_name = "none"`  
   - `item_price = 0`  
   - `item_quantity = 0`  
3. Define a **method** `print_item_cost()` that:  
   - Computes the total cost as `item_price × item_quantity`  
   - Displays output in the format:  
     *"[item_name] [item_quantity] @ $[item_price] = $[total_cost]"*

---

### Step 2: Create item objects from user input
1. Display: *"Item 1"*  
   - Prompt user for item name, price, and quantity.  
   - Validate input to ensure price and quantity are non-negative numeric values.  
   - Create `item1` object from `ItemToPurchase` class.

2. Display: *"Item 2"*  
   - Prompt user for item name, price, and quantity.  
   - Validate input similarly.  
   - Create `item2` object from `ItemToPurchase` class.

---

### Step 3: Compute and display total cost
1. Display: *"TOTAL COST"*  
2. Call `print_item_cost()` for both `item1` and `item2`.  
3. Compute **total** as `(item1.item_price × item1.item_quantity) + (item2.item_price × item2.item_quantity)`  
4. Display total in formatted output:  
   *"Total: $[total]"*

***End***

---

# Module 5: Critical Thinking Assignment

## Overview
The assignment is divided into two parts:  
Part 1 focuses on collecting and analyzing rainfall data using nested loops.  
Part 2 focuses on using conditional logic to calculate book club reward points based on the number of books purchased.  

All files for this assignment are organized within the following directory:  
`/Module5/CriticalThinking`  

---

## Part 1: Monthly Rainfall Data Collection
**Objective:**  
Write a Python program that uses nested loops to collect rainfall data and calculate the average rainfall over a given number of years.  
The outer loop should iterate once for each year, and the inner loop should iterate twelve times (once per month).  
After all iterations, the program should display the total number of months, total inches of rainfall, and the average monthly rainfall across the entire period.

**Files Included:**  
- `monthly_rainfall.py` — Python source file for Part 1  

**Pseudocode:**

***Begin***

1. Display header: *"Monthly Rainfall Data Entry"*  

2. Prompt user to **enter the number of years**  
   - Convert input to an integer.  
   - If the value is less than or equal to zero, display error:  
     *"Number of years must be a positive integer."*  
   - Exit program on invalid input.  

3. Initialize variable **total_rainfall = 0.0**  

4. **For each year (outer loop):**  
   1. Display the year number.  
   2. Initialize **month_index = 0**.  

   3. **While month_index < 12 (inner loop):**  
      - Prompt user to **enter rainfall (in inches)** for the current month.  
      - Convert input to a float.  
      - If the value is negative, display error:  
        *"Rainfall must be a non-negative number."*  
        - Prompt again until valid input is entered.  
      - Add the valid rainfall amount to **total_rainfall**.  
      - Increment **month_index** by 1.  

5. After both loops complete:  
   - Compute **total_months = num_years × 12**  
   - Compute **average_rainfall = total_rainfall ÷ total_months**  

6. Display the results:  
   - *"Total number of months: [total_months]"*  
   - *"Total inches of rainfall: [total_rainfall]"*  
   - *"Average monthly rainfall: [average_rainfall]"*  

***End***

---

## Part 2: Book Club Rewards
**Objective:**  
Write a Python program that calculates the number of reward points earned based on the number of books purchased in a month.  
The program should prompt the user for the number of books purchased and then award points according to the following rules:

- 0 books → 0 points  
- 2 books → 5 points  
- 4 books → 15 points  
- 6 books → 30 points  
- 8 or more books → 60 points  

**Files Included:**  
- `book_club_rewards.py` — Python source file for Part 2  

**Pseudocode:**

***Begin***

1. Display header: *"Book Club Rewards"*

2. Prompt user to **enter the number of books purchased this month**  
   - Convert input to an integer.  
   - If the value is negative, display error:  
     *"Number of books purchased must be non-negative."*  
   - Exit program on invalid input.

3. Initialize **reward_points_earned = 0**

4. Use conditional logic to determine points:  
   - If **books_purchased >= 8**, set **reward_points_earned = 60**  
   - Else if **books_purchased >= 6**, set **reward_points_earned = 30**  
   - Else if **books_purchased >= 4**, set **reward_points_earned = 15**  
   - Else if **books_purchased >= 2**, set **reward_points_earned = 5**  
   - Else, keep **reward_points_earned = 0**

5. Display the result:  
   - *"Reward points earned: [reward_points_earned]"*

***End***

---

# Module 6: Portfolio Milestone

## Overview
This milestone continues the online shopping cart project by introducing a `ShoppingCart` class and a menu-driven interface that allows users to add, remove, modify items, and display cart information.  
All files for this assignment are organized within the following directory:  
`/Module6/PortfolioMilestone`

---

## Online Shopping Cart

**Objective:**  
Write a Python program that expands the shopping cart system using an `ItemToPurchase` class and a new `ShoppingCart` class. The program should provide a text menu to add items, remove items, change item quantities, output item descriptions, and output the full shopping cart summary.

**Files Included:**  
- `shopping_cart.py` — Python source file for this milestone

**Pseudocode:**

***Begin***

### Step 4: Build the `ShoppingCart` class
1. Create class **ShoppingCart** with attributes:  
   - `customer_name` (string) — default `"none"`  
   - `current_date` (string) — default `"January 1, 2020"`  
   - `cart_items` (list of `ItemToPurchase`)
2. Implement methods:  
   - `add_item(item: ItemToPurchase)` — append item to `cart_items`.  
   - `remove_item(item_name: str)` — remove matching item by name; if not found, display:  
     *"Item not found in cart. Nothing removed."*  
   - `modify_item(item: ItemToPurchase)` — update matching item’s description, price, and/or quantity if provided; if not found, display:  
     *"Item not found in cart. Nothing modified."*  
   - `get_num_items_in_cart()` — return the sum of all item quantities in the cart
   - `get_cost_of_cart()` — return total cost across all items.  
   - `print_total()` — output cart heading, itemized costs, and total; if empty, display:  
     *"SHOPPING CART IS EMPTY"*  
   - `print_descriptions()` — output cart heading and each item’s description.

---

### Step 5: Implement `print_menu(cart: ShoppingCart)`
1. Display menu:
   ```
   MENU
   a - Add item to cart
   r - Remove item from cart
   c - Change item quantity
   i - Output items' descriptions
   o - Output shopping cart
   q - Quit
   ```
2. Prompt for a single-character option; on invalid input, re-prompt.  
3. Continue processing options until the user enters `q` (Quit).

---

### Step 6: Implement menu options
- **a (Add item):** Prompt for name, description, price, quantity; create `ItemToPurchase`; call `add_item()`.  
- **r (Remove item):** Prompt for item name; call `remove_item()`.  
- **c (Change item quantity):** Prompt for item name and new quantity; call `modify_item()`.  
- **i (Output items’ descriptions):** Call `print_descriptions()`.  
- **o (Output shopping cart):** Call `print_total()`.

***End***

---
