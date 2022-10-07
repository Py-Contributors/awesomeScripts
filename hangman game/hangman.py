# Title :- The Hangaman game using python

# importing all the required libraries
from words import Word


print('This is the Hangman game You have got 7 chances to guess the Color')
print('BEST OF LUCK!!.. Enjoy the game..')


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
WORD_TO_GUESS = Word()
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
