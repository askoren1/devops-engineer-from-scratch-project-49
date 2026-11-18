import prompt

ROUNDS_TO_WIN = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
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
