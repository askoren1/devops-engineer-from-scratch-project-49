from secrets import randbelow

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = MIN_NUMBER + randbelow(MAX_NUMBER - MIN_NUMBER + 1)
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer
