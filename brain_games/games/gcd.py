from secrets import randbelow

RULES = "Find the greatest common divisor of given numbers."
MAX_NUMBER = 100


def find_gcd(first, second):
    while second:
        first, second = second, first % second
    return first


def generate_round():
    first = randbelow(MAX_NUMBER) + 1
    second = randbelow(MAX_NUMBER) + 1

    question = f"{first} {second}"
    answer = find_gcd(first, second)
    return question, str(answer)
