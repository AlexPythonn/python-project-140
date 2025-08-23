import random
from prompt_toolkit import prompt
from  brain_games.cli import  welcome_user

def calculate():
    name = welcome_user()
    print('What is the result of the expression? ')
    
    for i in range(3):
        operadores = ['+', '-', '*']
        operador = random.choice(operadores)
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        print(f"Question: {num1} {operador} {num2}")
        answer = prompt('Your answer: ')    
        if int(answer) == resultado:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{resultado}'.\nLet's try again, {name}!")
            return
    print(f"Congratulations, {name}!")