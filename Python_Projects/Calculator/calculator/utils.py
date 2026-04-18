def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def print_result(operation_name, result):
    print(f"\nThe result of {operation_name} is: {result}")
