"""Grade Calculator"""

grades = [85, 92, 78, 90, 65]

for grade in grades:
    if grade <= 70:
        print(f"Grade: {grade}: Needs Improvement")
    else:
        print(f"Grade: {grade}")
