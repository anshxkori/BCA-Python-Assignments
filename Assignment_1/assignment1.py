# ------------------------------------------------------
# Project Title: Daily Calorie Tracker CLI
# Course: Programming for Problem Solving using Python
# Author: Ansh Kori
# Roll no.: 2501060063
# Serial no.: 25
# Section: 'B'
# Date: 29 November 2025
# ------------------------------------------------------

import datetime

print("\n====================================================")
print("      WELCOME TO DAILY CALORIE TRACKER (CLI)")
print("====================================================")
print("This tool helps you store your meal names & calories,")
print("calculate total and average calories and compare it")
print("with your daily calorie limit.\n")

# ---------- Task 2: Input & Data Collection ----------
meals = []
calories = []

num = int(input("How many meals do you want to enter today? "))

for i in range(num):
    print(f"\nEnter details for meal {i + 1}:")
    meal_name = input("Meal Name: ")
    calorie_amount = float(input("Calories (in numbers): "))
    meals.append(meal_name)
    calories.append(calorie_amount)

# ---------- Task 3: Total, Average & Comparison ----------
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# ---------- Task 4: Warning System ----------
if total_calories > daily_limit:
    limit_status = "⚠️ WARNING: You have exceeded your daily calorie limit!"
else:
    limit_status = "✔ You are within your daily calorie limit. Good job!"

# ---------- Task 5: Formatted Output ----------
print("\n====================================================")
print("                CALORIE SUMMARY REPORT")
print("====================================================")
print("Meal Name\tCalories")
print("-----------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("-----------------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{round(average_calories, 2)}")
print("-----------------------------------------------")
print(limit_status)
print("====================================================\n")

# ---------- Task 6: BONUS - Save to File ----------
save = input("Do you want to save this session to a file? (yes/no): ").lower()

if save == "yes":
    calorietracker = "calorie_log.txt"
    filename = "calorie_log.txt"
with open(filename, "a", encoding="utf-8") as file:
    file.write("====================================================\n")
    file.write("       CALORIE SUMMARY LOG - DAILY TRACKER\n")
    file.write("====================================================\n")
    file.write("Timestamp: " + str(datetime.datetime.now()) + "\n\n")
    file.write("Meal Name\tCalories\n")
    file.write("-----------------------------------------------\n")
    for i in range(len(meals)):
        file.write(f"{meals[i]}\t\t{calories[i]}\n")
    file.write("-----------------------------------------------\n")
    file.write(f"Total:\t\t{total_calories}\n")
    file.write(f"Average:\t{round(average_calories, 2)}\n")
    file.write(limit_status + "\n")
    file.write("====================================================\n\n")

    print(f"\n📌 Session saved successfully in '{filename}'")

print("\nThank you for using the Daily Calorie Tracker! Stay Healthy 💪")
