import random

while True:
    roll = input('a. role \nb. no \nAns.')
    if roll == 'a':
        print('\033[33m' + str(random.randint(1, 6)) + '\033[0m')
    else:
        print('\033[33m' + 'ok' + '\033[0m')
        break