import random

from prompt_toolkit import prompt

from brain_games.cli import welcome_user


def is_prime(n: int) -> bool:
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    rounds = 3  # número de preguntas que se le hacen al jugador
    for _ in range(rounds):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt("Your answer: ")

        correct_answer = "yes" if is_prime(number) else "no"

        if answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'")
            print(f"Let's try again,{name}!")
            return

    print(f"Congratulations, {name}!")