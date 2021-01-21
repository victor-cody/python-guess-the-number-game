#! python
# this is a guess the number game

import math
import asyncio
import random

global game_playing
game_playing = True
print('-- Welcome to the game 😀 --')

manuel = '''
In this game you are to gusses the correct number that is chosen from the range \n 1 - 100. Good Luck 😀
'''
print(manuel.strip())

number_list = list(range(1, 101))
correct_num = random.choice(number_list)

#our function for the computer to pick a random number the random.randrange function
def chose_correct_number(arr:int):
    """
    using the random.randrange(self, start: int, stop: Union[int, None]=..., step: int=...) function that Choose a random item from range(start, stop[, step]).
	our arr argument here is the  number_list list
    """
    correct_num = number_list[arr]
    return correct_num

global count
count = 6

async def choose():
    # using the global statement to make my variables non-local
    global user_choice
    global computer_choice

    user_choice = int(input('what number do you choose\n'))
    await asyncio.sleep(0.58)
    computer_choice = chose_correct_number(correct_num)

def validate(choice1,choice2):
    """
    function to check if our choice is higher, lower or equal to the correct choice 
    """
    if choice1 == choice2: #condition 1
        print(f'you gussed it right! 😀 \n the correct number is {choice2}')
        game_playing = False
        global count
        count = 0
    elif choice1 > choice2 : #condition 2
        print(f'the number {choice1} is higher than the correct number')
    else: #condition 3
        print(f'the number {choice1} is lower than the correct number')


while game_playing:
    rounds = 'rounds' if count > 1 else 'round' 
    print(f'you have {count} more {rounds}') # prints the number of rounds we have left depending on the rounds and count variable 
    count -= 1 # decrementing the number of rounds we have
    asyncio.run(choose())
    validate(user_choice,computer_choice)

    if count == 0 and user_choice != computer_choice:
        # deciding what will happen when we have run out if rounds and the user has not yet guessed the correct number
        game_playing = False
        print(f'you have run out chances :( \n the correct number is {computer_choice} ')

    elif count == 0 and user_choice == computer_choice:
        game_playing = False
        # print(f'you gussed it right! 😀 \n the correct number is {computer_choice}')

