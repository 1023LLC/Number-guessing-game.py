import random

top_of_range = input('Enter a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please enter a number greater than zero next time!')
        quit()
else:
    print('Please enter a number next time!')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    
    else:
        print('Please enter a number next time!')
        quit()
        continue
    
    if user_guess == random_number:
        print('Correct guess!')
        break
    else:
        print('Incorrect!')
        if user_guess > random_number:
            print('Guess is big, try a smaller number!')
        else:
            print('Guess is smaller, try a bigger number!')

if guesses < (0.5 * top_of_range):
    print(f'You got it in {guesses} guesses!, You are good at making guesses!👍️')
else:
    print(f'You got it in {guesses} guesses!, You suck at making guesses!😂')
