
from prompt_toolkit import prompt

def welcome_user():
   
   name = prompt('May I have your name? ')
   print(f"Hello, {name}!")
   
   return name