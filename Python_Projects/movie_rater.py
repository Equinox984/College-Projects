"""The Movie Rater"""

# Constants
SEPARATOR = "==============================="
RESULTS_HEADER = "===== Results ====="
WELCOME_MESSAGE = "Hello! Welcome to Equinox Movie Rater!"
AGE_PROMPT = "Write your Age -> "
INVALID_AGE_MESSAGE = "That's not a valid age. Please enter a number."


def get_age_rating(age: int) -> str:
    """
    Determines the movie rating based on the user's age.

    Args:
        age (int): The age of the user.

    Returns:
        str: The recommended movie rating.
    """
    if age < 7:
        return "You should watch G-rated movies."
    elif age < 13:
        return "You can watch PG-rated movies."
    elif age < 17:
        return "You can watch PG-13 rated movies."
    else:
        return "You can watch R-rated movies."


def main():
    """
    Main function to run the movie rater program.
    """
    print(SEPARATOR)
    print(WELCOME_MESSAGE)
    print(SEPARATOR, "\n")

    while True:
        user_input = input(AGE_PROMPT).strip()
        try:
            user_age = int(user_input)
            if user_age < 0:
                print(INVALID_AGE_MESSAGE)
                continue
            break  # Exit loop if age is valid
        except ValueError:
            print(INVALID_AGE_MESSAGE)

    print("\n", RESULTS_HEADER)
    print(get_age_rating(user_age), "\n")


if __name__ == "__main__":
    main()
