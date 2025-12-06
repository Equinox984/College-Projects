"""List Analyzer"""

separator = "===================================="

# Created the List of Numbers
numbers = [12, 5, 8, 19, 3, 15, 7]
largest_number = numbers[0]

# Find the largest number in the list
for number in numbers:
    if number > largest_number:
        largest_number = number

# Print the largest number
print(separator, "\n")
print(f"The largest number in the list is: {largest_number}\n")
print(separator, "\n")
print("The list in reverse order is like this: ", numbers[::-1])
print("\n")
print(separator)
