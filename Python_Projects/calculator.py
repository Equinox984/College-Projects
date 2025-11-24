"""Equinox Calculator"""

print("Hello! Welcome to Equinox Calculator \n")

try:
    n1 = float(input("Write the first number: \n").strip())
    n2 = float(input("Write the second number: \n").strip())
    add = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2
except (ValueError, ZeroDivisionError):
    print("Invalid input. Please enter a valid number.")
    exit()

print("\n")
print("===== Results =====")
print(f"""
The addition of the first and second number is: {add}
The substraction of the first and second number is: {sub}
The multiplication of the first and second number is: {mul}
The division of the first and second is: {div}
""")
