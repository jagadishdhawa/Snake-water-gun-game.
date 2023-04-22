
#THE SNAKE, WATER, GUN GAME -----------------------------------------><------------<>

import random

def game(computer,you):
    if computer == you :
        return None
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif computer == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Computer chosses succesfully :\n")   
randum = random.randint(1,3)
if randum == 1:
    computer= 's'
elif randum==2:
    computer='w'
else:
    computer="g"
you = input("Your turn : (Enter any one of these s / w / g)\n")
a = game(computer,you)

print(f'computer chosse--{computer}')
print(f'You chosse--{you}')

if a == None:
    print("The game is Tie .")
elif a:
    print("you won the game")
else:
    print("Computer win / You losse \nBetter luck next time .")