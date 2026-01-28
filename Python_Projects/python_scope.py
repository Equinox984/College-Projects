total = 0


def add(a, b):
    total = a + b
    return total # Using return instead of print


def main():
    final_addition = add(4, 6) # Using a variable to get result
    print(f"Final Total: {final_addition}") # Calling the variable


main()
