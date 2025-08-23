from prompt_toolkit import prompt
from  brain_games.cli import  welcome_user

def even_or_odd():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no". ')
    
    for i in range(3):
        num = prompt('Question: ')
        answer = prompt('Your answer: ') 
      
        if int(num) % 2 != 0 and answer.lower() == "yes"  
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name} !")
            return
        elif int(num) % 2 == 0 and answer.lower() == "no" :
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name} !")
            return
        else:
            print("Correct!")
    print(f"Congratulations, {name}!")