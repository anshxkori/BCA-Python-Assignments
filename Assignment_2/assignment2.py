
# Project: GradeBook Analyzer
# Course: Programming for Problem Solving using Python
# Name: Ansh Kori
# Roll no.: 2501060063
# Serial no.: 25 
# Section 'B'
# A CLI system to read student marks (manual / CSV), calculate statistics,
# assign grades, generate pass/fail lists and print formatted report.


import csv
import statistics

# -------------------- TASK 3: STATISTICAL FUNCTIONS --------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


# -------------------- TASK 4: GRADE ASSIGNMENT --------------------
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades


# -------------------- TASK 2: DATA INPUT METHODS --------------------
def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        score = int(input("Enter marks: "))
        marks[name] = score
    return marks

def csv_input():
    marks = {}
    filename = input("Enter CSV file name (example: students.csv): ")
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            marks[row[0]] = int(row[1])
    return marks


# -------------------- TASK 6: REPORT DISPLAY --------------------
def display_report(marks, grades):
    print("\nName\t\tMarks\tGrade\n--------------------------------------")
    for name in marks:
        print(f"{name:12}\t{marks[name]}\t{grades[name]}")
    print("--------------------------------------")


# -------------------- MAIN CLI LOOP --------------------
print("===== Welcome to GradeBook Analyzer =====")
while True:
    print("\nMenu:")
    print("1. Manual input of students")
    print("2. Load from CSV file")
    print("3. Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        marks = manual_input()
    elif choice == "2":
        marks = csv_input()
    elif choice == "3":
        print("Thank you for using GradeBook Analyzer!")
        break
    else:
        print("Invalid input. Try again.")
        continue

    # Statistics
    avg = calculate_average(marks)
    med = calculate_median(marks)
    highest = find_max_score(marks)
    lowest = find_min_score(marks)

    print("\n===== STATISTICAL SUMMARY =====")
    print(f"Average Score: {avg:.2f}")
    print(f"Median Score: {med}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")

    # Grades
    grades = assign_grades(marks)

    # Grade Distribution
    distribution = {g: list(grades.values()).count(g) for g in set(grades.values())}
    print("\n===== GRADE DISTRIBUTION =====")
    for g, count in distribution.items():
        print(f"{g}: {count} students")

    # Task 5: Pass / Fail (Using list comprehension)
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]

    print("\n===== PASS / FAIL RESULT =====")
    print(f"Passed ({len(passed)}): {passed}")
    print(f"Failed ({len(failed)}): {failed}")

    # Table
    display_report(marks, grades)

    again = input("\nRun analysis again? (yes/no): ")
    if again.lower() != 'y':
        print("Exiting the program. Goodbye!")
        break
