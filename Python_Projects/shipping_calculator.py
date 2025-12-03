"""Shipping Calculator"""

# Welcome Message
print("`\n")
separator = "===================================="
print(separator)
print("Hello! Welcome to your personal Shipping Calculator!")
print(separator, "\n")

# User Information Messages
weight = float(input("Enter the total weight (kg) of your order -> ").strip())
destination = int(
    input("Please choose your shipping destination (1 for Domestic/ 2 for International) -> ").strip())

# Domestic Calculation Process
if destination == 1:
    print("\nCalculating Domestic Shipping...\n")
    if weight <= 2:
        shipping_cost = 5.0
    elif weight <= 5:
        shipping_cost = 10.0
    else:
        shipping_cost = 15.0

# International Calculation Process
elif destination == 2:
    print("\nCalculating International Shipping...\n")
    if weight <= 1:
        shipping_cost = 15.0
    elif weight <= 3:
        shipping_cost = 25.0
    else:
        shipping_cost = 40.0

# Potential Error Message
else:
    print(f"\nERROR: Destination '{destination}' is not valid")
    # This helps us to avoid showing the results message in a case of an error
    shipping_cost = -1.0


# Results Message
if shipping_cost >= 0:
    print(separator)
    print(f"Shipping Destination: {destination}")
    print(f"Order Weight: {weight}kg")
    print(f"Your calculated shipping cost is: {shipping_cost}$")
    print(separator)
