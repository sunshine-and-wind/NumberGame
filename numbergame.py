import random
num = random.randint(0, 99)
print('\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nThis is the Number Game.\nI picked a number between 1 and 100.')
count=0
bc = 0

while True:
    guess = input('Try to guess it in 5 tries: ')
    try:
        iguess=float(guess)
    except:
        print('Invalid entry. You must enter a number.')
        count = count + 1
        bc = bc + 1
        if count == 5:
            print('\nToo many attempts and/or errors. Exiting program.')
            if bc >=3:
                print('\nCome back when you are serious about playing.')
            quit()
        continue

    count = count + 1
    if iguess==num:
        if count == 1:
            print('Congrats! You guessed my number in', count, 'attempt.')
            quit()
        elif count >=2:
            print('Congrats! You guessed my number in', count, 'attempts.')
        quit()

    elif iguess > num:
        print('My number is lower.')

    elif iguess < num:
        print('My number is higher.')

    if count == 5:
        print('Still wrong!!!\nToo many attempts!!! Exiting Program.')
        quit()
