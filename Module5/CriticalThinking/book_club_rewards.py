# CSC500 - Principles of Programming - Module 5 Critical Thinking Part 2
# Michael Spandrio
# 
# Book Club Rewards

def main():
    print("\nBook Club Rewards\n")

    try:
        books_purchased_this_month = int(input("Enter the number of books purchased this month: "))
        if (books_purchased_this_month < 0):
            raise ValueError("Number of books purchased must be non-negative.")
    except ValueError:
        print("\nInvalid input. Please enter a non-negative integer value for number of books purchased this month.\n")
        exit(1)

    reward_points_earned = 0;
    if books_purchased_this_month >= 8:
        reward_points_earned = 60
    elif books_purchased_this_month >= 6:
        reward_points_earned = 30
    elif books_purchased_this_month >= 4:
        reward_points_earned = 15
    elif books_purchased_this_month >= 2:
        reward_points_earned = 5

    print(f"\nReward points earned: {reward_points_earned}\n")

if __name__ == "__main__":
    main()