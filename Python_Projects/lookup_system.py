"""Student Information Lookup System"""


# Search for students and display their grade
def lookup_student(list_std, grades):
    if not list_std:
        print("\nSTATUS: Student list is empty.\n")
        return

    print("\n--- Student List ---")
    for std_index, student in enumerate(list_std):
        print(f"[{std_index}] {student}")
        
    while True:
        try:
            raw_input = input("\nEnter the student's index number (press Enter to cancel) ->>> ").strip()
            
            if not raw_input:
                print("\nSTATUS: Lookup cancelled.")
                break
                
            index = int(raw_input)
            student_name = list_std[index]
            grade = grades[student_name]
            print(f"\nSTATUS: {student_name}'s grade is {grade}")
            break
        except ValueError:
            print("\nERROR: Invalid input. Please enter a valid index number.\n")
        except IndexError:
            print("\nERROR: Student index out of range. Please try again.\n")
        except KeyError:
            print("\nERROR: Grade not found for the selected student.\n")

# Add students to the list
def add_student(list_std, grades):
    student_name = input("Enter the student's name (press Enter to cancel) ->>> ").strip()
    
    if not student_name:
        print("\nSTATUS: Add student cancelled.")
        return
        
    grade = input("Enter the student's grade (press Enter to skip) ->>> ").strip()
    list_std.append(student_name)
    
    if grade:
        grades[student_name] = grade
        print(f"\nSTATUS: Added {student_name} with grade {grade}.")
    else:
        print(f"\nSTATUS: Added {student_name} without a grade.")

# Remove students from the list
def remove_student(list_std, grades):
    student_name = input("Enter the student's name ->>> ").strip()
    if student_name in list_std:
        list_std.remove(student_name)
        if student_name in grades:
            del grades[student_name]
        print(f"\nSTATUS: {student_name} has been removed from the list.")
    else:
        print(f"\nSTATUS: {student_name} is not in the list.")

# MAIN FUNCTION
def main():
    list_std = []
    grades = {}
    
    while True:
        try:
            choice = int(input("""
===== Welcome to the Student Information Lookup System =====
            
[1] Lookup Student
[2] Add Student
[3] Remove Student
[4] Exit

-> """).strip())
            print("\n")

            # User's Decision on Menu
            if choice == 1:
                lookup_student(list_std, grades)
            elif choice == 2:
                add_student(list_std, grades)
            elif choice == 3:
                remove_student(list_std, grades)
            elif choice == 4:
                break
            else:
                print("ERROR: Select 1, 2, 3, or 4!!!")

        except ValueError:
            print("\nERROR: Invalid Option. Select 1, 2, 3, or 4!!!\n")
            continue

main()
