separator = "============================="
print("\n", separator)
print("Welcome to Equinox Grade Feedback Program!")
print(separator, "\n")

# Asking the User Score
userScore = float(input("Please enter your grade for analysis: \n"))

# Results
print("\nCalculating...\n")
if userScore >= 90:
    print("Excellent. You are awesome!")
elif userScore >= 70:
    print("Good. Decent result.")
else:
    print("Needs Improvement.")
