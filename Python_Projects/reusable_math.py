"""Function Addition"""


def addition(a, b):
    return a + b


def substraction(a, b):
    return a - b


def result():
    while True:
        try:
            # Addition Functionality
            n1 = float(input("What's x (ADD) ? -> "))
            n2 = float(input("What's y (ADD)? -> "))
            result_add = addition(n1, n2)

            # Substraction Functionality
            n3 = float(input("What's x (SUBSTRACT)? -> "))
            n4 = float(input("What's y (SUBSTRACT)? -> "))
            result_sub = substraction(n3, n4)
            break
        except ValueError:
            print("ERROR: Write a Valid Number!")
            continue

    # Results
    print(f"The result for addition is {result_add} and substraction is {result_sub}")


result()
