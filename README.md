# CSC500-Principles-of-Programming
Course Assignments - Part of CSU Global Master's in AI &amp; ML Program

# Module 1: Critical Thinking Assignment

## Overview
The assignment is divided into two parts: Part 1 focuses on addition and subtraction, and Part 2 focuses on multiplication and division.  

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
