from secrets import randbelow

import prompt

ROUNDS_TO_WIN = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def play():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS_TO_WIN):
        number = MIN_NUMBER + randbelow(MAX_NUMBER - MIN_NUMBER + 1)
        correct_answer = "yes" if is_even(number) else "no"

        print(f"Question: {number}")
        answer = input("Your answer: ")

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
    