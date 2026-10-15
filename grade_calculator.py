# Grade Calculator
# Calculates total marks, percentage, grade and pass/fail result.

PASS_PERCENTAGE = 50
SUBJECTS = ["Math", "Science", "English", "History", "Art"]


# function to calculate grade from percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


# function to get marks for each subject from the user with validation
def get_marks():
    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return marks


# function to print a report card
def print_report_card(marks):
    total_marks = sum(marks.values())
    maximum_marks = len(marks) * 100
    percentage = total_marks / len(marks)
    grade = calculate_grade(percentage)
    result = "Pass" if percentage >= PASS_PERCENTAGE else "Fail"

    print("\n------ REPORT CARD ------")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")

    print(f"\nTotal Marks: {total_marks} / {maximum_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")


def main():
    print("=== Student Grade Calculator ===")
    marks = get_marks()
    print_report_card(marks)


if __name__ == "__main__":
    main()