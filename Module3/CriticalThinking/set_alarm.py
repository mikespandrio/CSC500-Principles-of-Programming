# CSC500 - Principles of Programming - Module 3 Critical Thinking Part 2
# Michael Spandrio
# 
# Calculate alarm hour given current hour (24-hour clock) and hours to wait
import sys

def main():
    print("This program calculates the time your alarm will sound based on the current hour (on a 24-hour clock) and hours to wait.\n")

    time_in_hours = None
    hours_to_wait = None

    # input with error handling
    try:
        time_in_hours = int(input("\nEnter the current hour of the day (24-hour clock): "))
        if time_in_hours < 0 or time_in_hours > 23:
            raise ValueError("Hour must be between 0 and 23 (inclusive).")
    except ValueError:
        print("\nInvalid input. Please enter an integer value between 0 and 23 (inclusive).\n")
        sys.exit(1)

    try:
        hours_to_wait = int(input("\nEnter the number of hours to wait until alarm sounds: "))
        if hours_to_wait <= 0:
            raise ValueError("Number of hours to wait must be positive")
    except ValueError:
        print("\nInvalid input. Please enter a positive integer value.\n")
        sys.exit(1)


    # calculate the hour alarm will sound
    alarm_hour = (time_in_hours + hours_to_wait) % 24

    print("\nThe alarm will sound at {}:00 (based on 24-hour clock).\n".format(alarm_hour))

if __name__ == "__main__":
    main()