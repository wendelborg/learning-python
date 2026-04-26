def get_int_input(description: str) -> int:
    while True:
        try:
            return int(input(description))
        except ValueError:
            print("That was not a valid number, try again.")
