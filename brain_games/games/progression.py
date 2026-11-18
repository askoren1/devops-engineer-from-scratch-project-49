from secrets import randbelow

RULES = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10
MAX_START = 20
MAX_STEP = 10


def make_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    start = randbelow(MAX_START) + 1
    step = randbelow(MAX_STEP) + 1
    numbers = make_progression(start, step, PROGRESSION_LENGTH)

    hidden_index = randbelow(len(numbers))
    correct_answer = str(numbers[hidden_index])

    parts = [str(number) for number in numbers]
    parts[hidden_index] = ".."

    return " ".join(parts), correct_answer
