import turtle


def line(a, b, x, y):
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)


def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def draw_x(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def draw_o(x, y):
    turtle.up()
    turtle.goto(x + 67, y + 5)
    turtle.down()
    turtle.circle(62)


def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200


def calc_index(x, y):
    "Convert (x,y) coordinates to tiles index."
    return int((x+200)//133) + ((y+200)//133*3)


def is_winner(player, List):
    ''' RETURN TRUE IF player WIN '''
    return ((List[0] == player and List[1] == player and List[2] == player) or
            (List[3] == player and List[4] == player and List[5] == player) or
            (List[6] == player and List[7] == player and List[8] == player) or
            (List[0] == player and List[3] == player and List[6] == player) or
            (List[1] == player and List[4] == player and List[7] == player) or
            (List[2] == player and List[5] == player and List[8] == player) or
            (List[0] == player and List[4] == player and List[8] == player) or
            (List[2] == player and List[4] == player and List[6] == player)
            )


def show_winner(string):
    turtle.goto(0, -25)
    turtle.clear()
    turtle.color('red')
    turtle.down()
    turtle.write(string, align='center', font=("Arial", 50, "normal"))
    turtle.done()
    exit()


state = {'player': True}
players = [draw_x, draw_o]
taken = {0: None, 1: None, 2: None, 3: None,
         4: None, 5: None, 6: None, 7: None, 8: None}


def tap(x, y):
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    index = int(calc_index(x, y))
    if not taken[index]:
        player = state['player']
        draw = players[player]
        draw(x, y)
        taken[index] = player
        turtle.update()
        state['player'] = not player

    if is_winner(True, taken):
        show_winner(('O Won!'))
    elif is_winner(False, taken):
        show_winner(('X Won!'))


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
