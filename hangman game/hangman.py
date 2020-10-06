# Title :- The Hangaman game using python

# importing all the required libraries
from random import randint

print('This is the Hangman game You have got 7 chances to guess the Color')
print('BEST OF LUCK!!.. Enjoy the game..')

# list of the words to guess
WORD_LIST = {
    'rand_word_1': 'red',
    'rand_word_2': 'blue',
    'rand_word_3': 'green',
    'rand_word_4': 'yellow',
    'rand_word_5': 'orange',
    'rand_word_6': 'white',
    'rand_word_7': 'indigo',
    'rand_word_8': 'purple',
    'rand_word_9': 'black',
    'rand_word_10': 'gray'
}

# hangman tuple to display if user guesses wrong words.
HANGMAN = (
    """
    x-------x
    """,
    """
    x-------x
    |
    |
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    GAME OVER
    """
)


MAX = len(HANGMAN) - 1
num = randint(1, 10)
num_string = str(num)
words = 'rand_word_{}'.format(num_string)
WORD_TO_GUESS = WORD_LIST[words]
HIDDEN = ['_'] * len(WORD_TO_GUESS)
LETTERS_GUESSED = []


def start_game():
    # start game function to play the game
    hang_size = 0
    word_arr = list(WORD_TO_GUESS)

    while hang_size < MAX:
        print(str(HIDDEN))
        user_guess = input('Guess a letter: ')

        if user_guess in LETTERS_GUESSED:
            print('You already guessed it.. PLEASE PAY ATTENTION!')
            user_guess = input('Guess a letter: ')

        if user_guess in word_arr:
            print("Going well!.. It's in the word....Excellent work!")

            for num in range(len(word_arr)):
                if user_guess == word_arr[num]:
                    HIDDEN[num] = user_guess
                    if HIDDEN.count('_') == 0:
                        print('--------------BRILLIANT YOU WIN..!-------------')
                        print('************** Congratulations ****************')
                        quit()

        else:
            print("{}.. You have tried the BEST but.. Not in my word..".format(user_guess))
            hang_size += 1
            print(HANGMAN[hang_size])


# start_game function called
start_game()
