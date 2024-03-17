import datetime

def add_exercise():
    exercise_name = input("Enter exercise name: ")
    duration = float(input("Enter exercise duration (in minutes): "))
    with open("exercise_log.txt", "a") as file:
        file.write(f"{datetime.date.today()}, {exercise_name}, {duration}\n")
    print("Exercise logged successfully!")

def log_calories():
    calorie_intake = float(input("Enter calorie intake for today: "))
    with open("calorie_log.txt", "a") as file:
        file.write(f"{datetime.date.today()}, {calorie_intake}\n")
    print("Calories logged successfully!")

def view_summary():
    today = datetime.date.today()
    exercise_total = 0
    calorie_total = 0

    # Calculate exercise duration for today
    with open("exercise_log.txt", "r") as file:
        for line in file:
            date, _, duration = line.strip().split(", ")
            if date == str(today):
                exercise_total += float(duration)

    # Calculate calorie intake for today
    with open("calorie_log.txt", "r") as file:
        for line in file:
            date, calorie_intake = line.strip().split(", ")
            if date == str(today):
                calorie_total += float(calorie_intake)

    print(f"Exercise duration today: {exercise_total} minutes")
    print(f"Calorie intake today: {calorie_total} calories")

def view_exercises():
    date_input = input("Enter date (YYYY-MM-DD) to view exercises: ")
    try:
        target_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        with open("exercise_log.txt", "r") as file:
            print(f"Exercises done on {target_date}:")
            for line in file:
                date, exercise_name, duration = line.strip().split(", ")
                if date == str(target_date):
                    print(f"{exercise_name}: {duration} minutes")
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")

def main():
    while True:
        print("\nFitness Tracker")
        print("1. Add Exercise")
        print("2. Log Calories")
        print("3. View Daily Summary")
        print("4. View Exercises for a Day")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_exercise()
        elif choice == "2":
            log_calories()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            view_exercises()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
