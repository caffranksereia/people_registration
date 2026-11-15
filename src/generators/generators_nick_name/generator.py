import random


def generate_nickname(name: str) -> str:
    symbols = "!@#$%&*"

    first_letter = name[0].lower()
    middle_letter = name[len(name) // 2].lower()
    last_letter = name[-1].lower()

    first_number = random.randint(0, 9)
    second_number = random.randint(0, 9)

    first_symbol = random.choice(symbols)
    second_symbol = random.choice(symbols)

    nickname = (
        first_letter
        + str(first_number)
        + first_symbol
        + middle_letter
        + str(second_number)
        + second_symbol
        + last_letter
    )

    return nickname


def process_nickname() -> None:
    name = input("What's your name? ").strip()
    if name:
        print(generate_nickname(name))
    else:
        print("Name cannot be empty.")
