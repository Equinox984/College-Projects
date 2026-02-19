"""Safe Program CW - Computer Science Q3"""


def calculator():
    while True:
        try:
            print("\n===== Welcome to the Division Calculator =====")

            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the secind number: "))
            if num2 == 0:
                print("ERROR: You can't divide by zero.")
                continue

            result = num1 / num2

        except ZeroDivisionError:
            print("ERROR: You can't divide by zero dude.")

        except ValueError:
            print("ERROR: Write a number dude.")
            continue

        else:
            print(f"Result: {result}")

        print("Program finished succesfully!")
        break


calculator()
