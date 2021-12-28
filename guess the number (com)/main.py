import random


def user_guess(x):
    choice = random.randint(1, x)
    again = True
    while again:
        answer = True
        user_input = int(input(f'Pick your number (1-{x}) : '))
        print(f'\nYou pick : {user_input}')
        print(f'Com pick : {choice}')

        if user_input == choice:
            print('\nYou Win')
        else:
            print('\nYou Lose')

        while answer:
            play_again = input("\nWanna play again? (Y/N) ").upper()
            if play_again == 'Y':
                print('')
                again = True
                answer = False
            elif play_again == 'N':
                print('\n=====good bye=====')
                again = False
                answer = False
            else:
                print('\nWrong Answer')
                answer = True


# user_guess(5)


def computer_gues(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            choice = random.randint(low, high)
        else:
            choice = low
        print(f'com choice : {choice}')
        feedback = input('input: ').lower()
        if feedback == 'h':
            high = choice - 1
        elif feedback == 'l':
            low = choice + 1
    print('great job')


computer_gues(100)
