from operator import add, mul, sub
from secrets import choice, randbelow

RULES = "What is the result of the expression?"
MAX_OPERAND = 25
OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul,
}


def generate_round():
    left = 1 + randbelow(MAX_OPERAND)
    right = 1 + randbelow(MAX_OPERAND)
    symbol = choice(tuple(OPERATIONS))

    question = f"{left} {symbol} {right}"
    result = OPERATIONS[symbol](left, right)
    return question, str(result)
    