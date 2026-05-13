# In Bagels, a deductive logic game, you
# must guess a secret three-digit number
# based on clues. The game offers one of
# the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the
# wrong place, “Fermi” when your guess has a correct
# digit in the correct place, and “Bagels” if your guess
# has no correct digits. You have 10 tries to guess the
# secret number.
import random


def main():
    MAX_GUESS = 2

    while True:
        num_guess = 1
        RANDOM_NUM = random.randint(100, 999)

        print('''
        I am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues:
        When I say: That means:
            Pico One digit is correct but in the wrong position.
            Fermi One digit is correct and in the right position.
            Bagels No digit is correct.
        I have thought up a number.
        You have 10 guesses to get it.
        ''')

        while num_guess <= MAX_GUESS:
            user_guess = get_guess(num_guess)

            result = check_guess(str(RANDOM_NUM), user_guess)
            print(RANDOM_NUM, normalize_result(result))

            if user_guess == RANDOM_NUM:
                break
            num_guess += 1

            if num_guess > MAX_GUESS:
                print('You ran out of guesses')
                print(f'The correct number was {RANDOM_NUM}')

        play_again = input(
            'Do you want to play again? (press any key to continue except "n") ').lower()
        if play_again == 'n':
            break


def get_guess(num_guesses):
    while True:
        try:
            guess = int(input(f'Guess #{num_guesses} - '))
            if len(str(guess)) != 3:
                raise ValueError

            return str(guess)
        except ValueError:
            print('Please Enter a valid 3 digit number')


def check_guess(random_num, user_guess):
    result = []
    for index, char in enumerate(user_guess):
        if char == random_num[index]:
            result.append('Fermi')
        elif char in random_num:
            result.append('Pico')

    if not result:
        return ['Bagels']

    return result


def normalize_result(result):
    if all(x == 'Fermi' for x in result):
        return 'You got it!'

    return ' '.join(result)


if __name__ == '__main__':
    main()
