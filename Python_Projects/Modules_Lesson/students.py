from main import students

# # -------------------------
# Student Functions
# # -------------------------


def add_student(name):
    if name not in students:
        students[name] = []
        print(f"Student {name} added.")
    else:
        print("Student already exists.")


def remove_student(name):
    if name in students:
        del students[name]
        print(f"Student {name} removed.")
    else:
        print("Student not found.")


def display_students():
    if not students:
        print("No students available.")
    else:
        print("Students:")
        for student in students:
            print(f"- {student}")
