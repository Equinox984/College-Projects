"""The Movie Rater"""

# Welcome Message
separator = "==============================="
results = "===== Results ====="
print(separator)
print("Hello! Welcome to Equinox Movie Rater!")
print(separator, "\n")

# Process
user_age = int(input("Write your Age -> ").strip())
if user_age < 7:
    print("\n", results)
    print("You should watch G-rated movies.\n")

elif user_age < 13:
    print("\n", results)
    print("You can watch PG-rated movies.\n")

elif user_age < 17:
    print("\n", results)
    print("You can watch PG-13 rated movies.\n")

else:
    print("\n", results)
    print("You can watch R-rated movies.\n")
