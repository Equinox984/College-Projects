from operation import Addition, Multiplication
from utils import get_numbers, show_result

def main():
    a, b = get_numbers()

    add = Addition(a, b)
    mul = Multiplication(a, b)

    print("\n--- Results ---")
    show_result(add.calculate())
    show_result(mul.calculate())


    sub = Addition(a, -b) 
    print("Subtraction:", sub.calculate())


if __name__ == "__main__":
    main() 
##With `from` and `import` we can use `from` to call the file and `import` to extract the code inside the file.
##Everything becomes more organized.
##The entire program is within the calculator package. Separate the program with the init, operations module, main.py, and utils.