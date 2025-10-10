def main():
    # Output what the program will do
    print('This program will output the sum and difference of the two user-entered numbers.\n')

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

    # Compute sum and store in variable
    sum_of_nums = num1 + num2

    # Compute difference and store in variable
    diff_of_nums = num1 - num2
    
    # Output sum
    print('\nRESULTS:')
    print('The sum of', num1, 'and', num2, 'is:', sum_of_nums)

    # Output difference
    print('The difference between', num1, 'and', num2, 'is:', diff_of_nums, '\n')

if __name__ == '__main__':main()