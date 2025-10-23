import random

while True:
    roll = input("Press 'enter' to role, Press 'q' to quit")
    if roll == '':
        print('\033[33m' + str(random.randint(1, 6)) + '\033[0m')
    elif roll == 'q':
        print('\033[33m' + 'Thanks for playing!' + '\033[0m')
        break
    else:
        print('\033[33m' + 'Invaid input' + '\033[0m')