import math
import random

from prompt_toolkit import prompt

from brain_games.cli import welcome_user


def mcd():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    for i in range(3):
        num1 = abs(random.randint(1, 30))
        num2 = abs(random.randint(1, 30))
        print(f"Question: {num1} {num2}")
        resultado = math.gcd(num1, num2)
        answer = prompt("Your answer: ")
        if int(answer) == resultado:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{resultado}'")
            print(f"Let's try again,{name}!")
            return
    print(f"Congratulations, {name}!")
