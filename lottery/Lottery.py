import random

def game_player():
    guess_times = 0
    guessed_numbers = []
    print('this is a game, guess 3 numbers between 1-49')
    while guess_times < 3:
        num = input('enter a number :')
        guessed_numbers.append(num)
        guess_times += 1


    generated = []
    while len(generated) < 3:
        random_num = random.randrange(1, 50)
        generated.append(random_num)

    correct_guess = []
    for num in guessed_numbers:
        if num in generated:
            correct_guess.append(num)

    print('your correct guesses  are', correct_guess)
    print('you guessed ', guessed_numbers)
    print('the supposed are ', generated)

    num_correct = len(correct_guess)
    if num_correct < 3:
        points = num_correct * 5
        print('you got ' + str(points))
    else:
        points = 100
        print("JACKPOT WINNER!!!")
        print('you won all ' + str(points))
game_player()