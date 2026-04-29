from main import students

# -------------------------
# Grade Functions
# -------------------------


def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Added grade {grade} to {name}.")
    else:
        print("Student not found.")


def calculate_average(name):
    if name in students and students[name]:
        avg = sum(students[name]) / len(students[name])
        return avg
    return 0


def display_student_info(name):
    if name in students:
        print(f"\n{name}'s Grades: {students[name]}")
        avg = calculate_average(name)
        print(f"Average: {avg:.2f}")
    else:
        print("Student not found.")
