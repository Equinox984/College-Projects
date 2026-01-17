"""Function Practice Pack"""


# Create a function that calculates area of a rectangle
def calculate_rectangle_area(base, height):
    return base * height


# Create a function that converts Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Create a function that returns the larger of two numbers
def print_largest_number(number_1, number_2):
    if number_1 > number_2:
        print(f"\nThe largest number is: {number_1}")
    elif number_2 > number_1:
        print(f"\nThe largest number is: {number_2}")
    else:
        print("\nBoth numbers are equal.")


# Main Menu
while True:
    try:
        print("\n===== Function Pack Main Menu =====\n")
        print("1. Rectangle Area\n2. Celsius to Fahrenheit\n3. Largest Number\n4. Exit")
        main_choice = int(input("-> "))

        if main_choice == 1:
            base = float(input("\nBase of the Rectangle ->>> "))
            height = float(input("Height of the Rectangle ->>>  "))
            area = calculate_rectangle_area(base, height)
            print(f"\nThe Area of the Rectangle is: {area:.2f}")

        elif main_choice == 2:
            celsius = float(input("\nCelsius Temperature ->>>  "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Fahrenheit: {fahrenheit:.2f}")

        elif main_choice == 3:
            num1 = float(input("\nFirst number ->>> "))
            num2 = float(input("Second number ->>> "))
            print_largest_number(num1, num2)

        elif main_choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid option.")

    except ValueError:
        print("ERROR: Please enter a valid number.")
