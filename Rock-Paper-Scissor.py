import random

options = ['rock' , 'paper' , 'scissor']
scores = {'user' : 0 , 'computer' : 0}

def check_winner():
    if scores['user'] > scores['computer']:
        print('Play End. User Win!! ')
    elif scores['user'] < scores['computer']:
        print('Play End. Computer Win!! ')
    else:
        print('Play End.No Win!! ')
    exit()

print('Choose from this list: ' , options)

for i in range(10):
    computer = random.choice(options)
    user = input('Play the game: ')

    if (computer == 'rock' and user == 'scissor') or (computer == 'paper' and user == 'rock')\
         or (computer == 'scissor' and user == 'paper'):
        print('Computer win! ')
        scores['computer'] += 1
    elif computer == user:
        print('No win! Try again. ')
    else:
        print('User win! ')
        scores['user'] += 1

check_winner()