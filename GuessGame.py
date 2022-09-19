from random import randint


def generate_number(difficulty):
    return randint(1,difficulty)


def get_guess_from_user(difficulty):
    return int(input(f"please guess a number between 1 and {difficulty}\n"))


def compare_results(secret_number,user_input):
    return secret_number == user_input


def play(difficulty):
    secret_number=generate_number(difficulty)
    user_input=get_guess_from_user(difficulty)
    return compare_results(secret_number,user_input)



