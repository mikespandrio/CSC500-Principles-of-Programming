def main():
    # Output what the program will do
    print('This program will output the product and quotient of the two user-entered numbers.\n')

    # Take user inputs of two integer numbers
    num1 = None
    num2 = None

    try:
        num1 = int(input('Please enter an integer value: '))
    except ValueError:
        raise SystemExit('\nIncorrect input format. Please enter an integer value.\n')

    try:
        num2 = int(input('\nPlease enter another integer value: '))
    except ValueError:
        raise SystemExit('\nIncorrect input format. Please enter an integer value.\n')

    # Compute product and store in variable
    product_of_nums = num1 * num2

    # Output product
    print('\nRESULTS:')
    print('The product of', num1, 'and', num2, 'is:', product_of_nums)

    # Compute quotient and store in variable (check for division by 0)
    quotient_of_nums = None # Define variable before the try block
    try:
        quotient_of_nums = num1 / num2

        # Output quotient
        print('The quotient of', num1, 'and', num2, 'is:', quotient_of_nums, '\n')
    except ArithmeticError:
        raise SystemExit('\nCannot divide by zero, please re-run program and choose a different second number.\n')


if __name__ == '__main__':main()