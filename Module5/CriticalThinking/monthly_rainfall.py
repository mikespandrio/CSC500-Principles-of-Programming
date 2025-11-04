# CSC500 - Principles of Programming - Module 5 Critical Thinking Part 1
# Michael Spandrio
# 
# Monthly Rainfall

month_names = ["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"]


def main():
    print("\nMonthly Rainfall Data Entry\n")

    try:
        num_years = int(input("Enter the number of years of monthly rainfall data to input: "))
        if num_years <= 0:
            raise ValueError("Number of years must be a positive integer.")
    except ValueError:
        print("\nInvalid iput. Please enter a positive integer value for number of years.\n")
        exit(1)
    
    total_rainfall = 0.0
    for i in range(num_years):
        print(f"\nYear {i + 1}:")

        month_index = 0
        while month_index < 12:
            try:
                monthly_rainfall = float(input(f"Enter the rainfall for {month_names[month_index]} (in inches): "))
                if monthly_rainfall < 0:
                    raise ValueError("Rainfall must be a nnon-negative number.")
                total_rainfall += monthly_rainfall
                month_index += 1
            except ValueError:
                print("Invalid input. Please enter a non-negative numeric value for rainfall.")

    print(f"\nTotal number of months: {num_years * 12}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {total_rainfall / (num_years * 12)} inches\n")

if __name__ == "__main__":
    main()
