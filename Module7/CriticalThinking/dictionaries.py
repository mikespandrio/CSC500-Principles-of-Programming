# CSC500 - Principles of Programming - Module 7 Critical Thinking Assignment
# Michael Spandrio
#
# Course Lookup

course_rooms = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "CSC104": 1244,
    "CSC105": 1411
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "CSC104": "Burke",
    "CSC105": "Lee"
}

course_times = {
    "CSC101": "8:00 AM",
    "CSC102": "9:00 AM",
    "CSC103": "10:00 AM",
    "CSC104": "11:00 AM",
    "CSC105": "1:00 PM"
}

def main():
    course_number = input("\nEnter a course number: ")
    course_number = course_number.strip().upper()
    if course_number in course_rooms:
        print(f"\nCourse Number: {course_number}")
        print(f"Room Number: {course_rooms[course_number]}")
        print(f"Instructor: {course_instructors[course_number]}")
        print(f"Meeting Time: {course_times[course_number]}\n")
    else:
        print("\nA course with that course number does not exist. Please check the course number and try again.\n")

if __name__ == "__main__":
    main()

