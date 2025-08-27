from prompt_toolkit import prompt

from brain_games.cli import welcome_user


def even_or_odd():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no". ')

    for i in range(3):
        num = prompt("Question: ")
        while True:
            answer = prompt("Your answer: ")
            if answer in ("yes", "no"):
                break
            print("❌ Error: You can only answer 'yes' or 'no'.")
            print(f"Please try again {name}!")
            return
        if int(num) % 2 != 0 and answer.lower() == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name} !")
            return
        elif int(num) % 2 == 0 and answer.lower() == "no":
            print("'no' is wrong answer ;(."
                  " Correct answer was 'yes'.")
            print(f"Let's try again, {name} !")            
            return
        else:
            print("Correct!")
    print(f"Congratulations, {name}!")
