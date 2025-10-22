# CSC500-Principles-of-Programming
Course Assignments - Part of CSU Global Master's in AI &amp; ML Program

[Module 1: Critical Thinking Assignment](#module-1-critical-thinking-assignment)  
[Module 3: Critical Thinking Assignment](#module-3-critical-thinking-assignment)

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
