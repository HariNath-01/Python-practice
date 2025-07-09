'''import random
n=random.randrange(1,200)
print(f'Random number if {n}')
guess_num=int(input('Guess the number'))
while n!=guess_num:
    if(guess_num > n):
        print('Input if Too High , Try again')
    else:
        print('Input if Too Low , Try again')
    guess_num=int(input('Guess the number'))
print('You Won the game')'''

import random
n = random.randrange(1,100)
print(f'Random number if {n}')
guess_num = int(input('Guess the number'))
while n!=guess_num:
    if (guess_num>n):
        print('Input is high , try again')
    else:
        print('Input is low , try again')
    guess_num = int(input('Guess the number'))
print('you won')