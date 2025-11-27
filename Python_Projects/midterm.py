"""Midterm Python Exercise"""

# Welcome Message
separator = "============================="
print("\n", separator)
print("Welcome to Equinox Grade Feedback Program!")
print(separator, "\n")

# Asking the User Score
userScore = float(
    input("Please enter your grade for analysis (between 0 - 100): \n"))

# Results
print("\nCalculating...\n")

if userScore > 100 or userScore < 0:
    print("Impossible. Keep Dreaming")
elif userScore >= 90 and userScore <= 100:
    print("Excellent. You are awesome!")
elif userScore <= 70:
    print("Needs Improvement.")
else:
    print("Good. Decent Result")
