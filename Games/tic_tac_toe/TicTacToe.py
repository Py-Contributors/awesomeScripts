import os

x, y, turn = 0, 0, 0
BLANK = ' '
board = [[BLANK, BLANK, BLANK],
         [BLANK, BLANK, BLANK],
         [BLANK, BLANK, BLANK], ]


def win(player, O_X):
    global board
    check = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == O_X:
                check += 1
                if check == 3:
                    print(f'player {player} IS Win')
                    return 0
        check = 0

    for y in range(3):
        for x in range(3):
            if board[x][y] == O_X:
                check += 1
                if check == 3:
                    print(f'player {player} IS Win')
                    return 0
        check = 0
    if ((board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') | (
            board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X')):
        print(f"PLAYER {player} IS WIN")
        return 0
    return 1


def write(player, O_X):
    global turn, board
    turn += 1
    while True:
        print(f"PLAYER {player}'s turn(x y)")
        try:
            x, y = input("input x y : ").split()
        except IOError:
            print("retry")
            continue
        x = int(x)
        y = int(y)
        if x > 2 or y > 2:
            print("retry")
            continue
        if board[x][y] == BLANK:
            board[x][y] = O_X
            break
        else:
            print("Wrong Position !!\n")
            continue


def print_board():
    os.system('clear')
    os.system('cls')
    print("x|y [0]|[1]|[2]")
    for a in range(3):
        b = 0
        print("    ---|---|---")
        print(f'[{a}] {board[a][b]}  | {board[a][b + 1]} | {board[a][b + 2]} ')
    print("    ---|---|---")


def game():
    while (True):
        print_board()

        print(f'turn {turn}')
        if turn % 2 == 1:
            write(2, 'X')
            if win(2, 'X') == 0:
                print_board()
                return
        else:
            write(1, 'O')
            if win(1, 'O') == 0:
                print_board()
                return

        if turn == 9:
            print("Draw")
            print_board()
            return


game()
