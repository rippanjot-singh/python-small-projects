password = 'python'
trials = 5

while trials > 0:
    ui = input("enter your password: ")
    trials -=1
    if ui == password:
        print('login successful')
        break
    elif trials == 0:
        print('Trial limit reached! access blocked')
    else:
        print(f'try again! {trials} tries left')