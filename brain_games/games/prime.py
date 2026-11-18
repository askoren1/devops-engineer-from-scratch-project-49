from secrets import randbelow

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def generate_round():
    number = randbelow(MAX_NUMBER) + 1
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer
