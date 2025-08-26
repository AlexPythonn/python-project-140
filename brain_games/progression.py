import random

from prompt_toolkit import prompt

from brain_games.cli import welcome_user


def progre():
    name = welcome_user()
    print("What number is missing in the progression?")
    for i in range(3):
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        length = random.randint(5, 10)
        list = [start + i * step for i in range(length)]
        hidden_number = random.randrange(len(list))
        num = list[hidden_number]
        shown = [str(n) for n in list]
        shown[hidden_number] = ".."
        hidden_list = " ".join(shown)
        print(f"Question: {hidden_list}")
        answer = prompt("Your answer: ")
        if int(num) == int(answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{num}'")
            print(f"Let's try again,{name}!")
            return

    print(f"Congratulations, {name}!")