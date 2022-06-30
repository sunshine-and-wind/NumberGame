count=0
num=8

while True:
    guess = input('Guess my number? ')
    try:
        iguess=int(guess)
    except:
        print('Invalid entry. You must enter a number.')
        continue
    count == count+1

    if iguess == num:
        if count = 1:
             print('Congrats! You guessed my number in', count, 'attempt.')
        if 2 <= count <=5:
            print('Congrats! You guessed my number in', count+1, 'attempts.')
    elif count >= 5:
        print('Too many attempts. Try again later.')
        break

    if iguess > num:
        print('My number is lower.')
        continue
    if iguess < num:
        print('My number is higher.')
        continue
