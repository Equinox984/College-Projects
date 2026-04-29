# Student Management App (Monolithic Version)
# Your task: Refactor this into multiple modules!
from grade import add_grade, calculate_average, display_student_info
from students import add_student, display_students, remove_student

students = {}

# -------------------------
# Main Program
# -------------------------


def main():
    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Add Grade")
        print("4. Display Students")
        print("5. Display Student Info")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            remove_student(name)

        elif choice == "3":
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter grade: "))
                add_grade(name, grade)
            except ValueError:
                print("Invalid grade.")

        elif choice == "4":
            display_students()

        elif choice == "5":
            name = input("Enter student name: ")
            display_student_info(name)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
