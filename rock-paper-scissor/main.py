import random

computer = ['rock', 'paper', 'scissor']
print('Game started! press (q) to quit')
# print(computer[0])

uv = '\033[33m'+ 'User Win!' + '\033[0m'
cv = '\033[33m'+ 'Computer Win!' + '\033[0m'

while True:
    rcom = str(random.choice(computer))
    cp = ' Computer rolled: ' '\033[33m' + rcom + '\033[0m'

    user = input('(r) for rock \n(p) for paper \n(s)for scissor \n>>>')
    if user == rcom[0]:
        print('\033[33m'+ 'Its a draw!' + '\033[0m')   
    elif user == 'r' and rcom == 'paper':
        print(cv + cp)
    elif user == 'r' and rcom == 'scissor':
        print(uv + cp)
    elif user == 'p' and rcom == 'scissor':
        print(cv + cp)
    elif user == 'p' and rcom == 'rock':
        print(uv + cp)
    elif user == 's' and rcom == 'rock':
        print(cv + cp)
    elif user == 's' and rcom == 'paper':
        print(uv + cp)
    elif user == 'q':
        print('\033[33m'+ 'Thanks for playing!' + '\033[0m')
        break
    else:
        print('\033[33m'+ 'Invalid Input' + '\033[0m')