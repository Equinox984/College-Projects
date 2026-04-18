from calculator.operations import Addition, Division, Multiplication, Subtraction
from calculator.utils import get_number, print_result


def main():
    while True:
        try:
            choice = int(
                input("""
--- Welcome to Equinox Calculator ---
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
[5] Exit

Enter your choice (1-5) -> """)
            )
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            a = get_number("Enter first number -> ")
            b = get_number("Enter second number -> ")
            op = Addition(a, b)
            print_result("Addition", op.calculate())
        elif choice == 2:
            a = get_number("Enter first number -> ")
            b = get_number("Enter second number -> ")
            op = Subtraction(a, b)
            print_result("Subtraction", op.calculate())
        elif choice == 3:
            a = get_number("Enter first number -> ")
            b = get_number("Enter second number -> ")
            op = Multiplication(a, b)
            print_result("Multiplication", op.calculate())
        elif choice == 4:
            a = get_number("Enter first number -> ")
            b = get_number("Enter second number -> ")
            try:
                op = Division(a, b)
                print_result("Division", op.calculate())
            except ZeroDivisionError:
                print("\nERROR: Cannot divide by zero.")
        elif choice == 5:
            print("\nBye! See you next time.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
