import turtle
import math
import random
import pickle
from collections import namedtuple


def draw_rect(x1, y1, x2, y2, text, textX, textY, text_size=20, text_color="white", color="#0cf54a",
              border_color="#09db41", border_size=0.05):
    pointer.fillcolor(border_color)
    pointer.begin_fill()

    pointer.goto(x1, y1)

    pointer.goto(x2, y1)
    pointer.goto(x2, y2)
    pointer.goto(x1, y2)
    pointer.goto(x1, y1)

    pointer.end_fill()

    pointer.fillcolor(color)
    pointer.begin_fill()

    pointer.goto(x1 + border_size, y1 + border_size)

    pointer.goto(x2 - border_size, y1 + border_size)
    pointer.goto(x2 - border_size, y2 - border_size)
    pointer.goto(x1 + border_size, y2 - border_size)
    pointer.goto(x1 + border_size, y1 + border_size)

    pointer.end_fill()

    pointer.color(text_color)
    pointer.goto(textX, textY)
    pointer.write(text, True, align="center", font=("Comic Sans", text_size, "bold"))


def draw_button(button_callback, x1, y1, x2, y2, text, textX, textY, text_size=20, text_color="white", color="#0cf54a",
                border_color="#09db41", border_size=0.05):
    draw_rect(x1, y1, x2, y2, text, textX, textY, text_size, text_color, color, border_color, border_size)
    current_buttons.append(Button(x1, y1, x2, y2, button_callback))


def draw_line(x1, y1, x2, y2, color="#636E72", pensize=5):
    pointer.pensize(pensize)
    pointer.color(color)
    pointer.up()
    pointer.goto(x1, y1)
    pointer.down()
    pointer.goto(x2, y2)
    pointer.up()


def check_win_row(win_rows):
    global winner

    if win_rows[0] != 0 and win_rows.count(win_rows[0]) == len(win_rows):
        if win_rows[0] == 1:
            winner = 1
        else:
            winner = 2

        return True
    return False


def check_ai_row(ai_rows):
    global ai_index

    if (ai_rows.count(1) == 2 or ai_rows.count(2) == 2) and ai_rows.count(0) == 1:
        ai_index = ai_rows.index(0)
        return True

    return False


def check_win():
    global squares
    global current_buttons
    global Button

    if (
            check_win_row(squares[0]) or check_win_row(squares[1]) or check_win_row(squares[2]) or
            check_win_row([squares[0][0], squares[1][0], squares[2][0]]) or
            check_win_row([squares[0][1], squares[1][1], squares[2][1]]) or
            check_win_row([squares[0][2], squares[1][2], squares[2][2]]) or
            check_win_row([squares[0][0], squares[1][1], squares[2][2]]) or
            check_win_row([squares[0][2], squares[1][1], squares[2][0]])):

        if (winner == 1):
            draw_rect(0.8, 1, 2.2, 2, "X wins!", 1.5, 1.5)
        elif winner == 2:
            draw_rect(0.8, 1, 2.2, 2, "O wins!", 1.5, 1.5)

        draw_button(restart, 1.1, 1.25, 1.45, 1.4, "RESTART", 1.275, 1.3125, 5, "white", "#09aedb", "#098edb", 0.01)
        draw_button(draw_main_menu, 1.5, 1.25, 1.85, 1.4, "MENU", 1.675, 1.3125, 5, "white", "#fc1303", "#db1c0f", 0.01)


def on_click_ai(x, y):
    global player1Turn, ai_index
    global squares
    global winner
    global current_buttons

    for button in current_buttons:
        if button.x1 < x < button.x2 and button.y1 < y < button.y2:
            button.on_click()
            current_buttons.remove(button)
            return

    if winner != 0:
        return

    if (x % 1 > 0.9 or x % 1 < 0.1) or (y % 1 > 0.9 or y % 1 < 0.1):
        return

    squareX = int(math.floor(x))
    squareY = int(math.floor(y))

    square = squares[squareX][squareY]

    if (square != 0):
        return

    pointer.goto(squareX + 0.5, squareY + 0.5)

    draw_line(squareX + 0.25, squareY + 0.75, squareX + 0.75, squareY + 0.25, "#34ebe8", 15)
    draw_line(squareX + 0.25, squareY + 0.25, squareX + 0.75, squareY + 0.75, "#34ebe8", 15)

    player1Turn = False
    squares[squareX][squareY] = 1

    squareX = 100
    squareY = 100

    if check_ai_row(squares[0]):
        squares[0][ai_index] = 2

        squareX = 0
        squareY = ai_index
    elif check_ai_row(squares[1]):
        squares[1][ai_index] = 2

        squareX = 1
        squareY = ai_index
    elif check_ai_row(squares[2]):
        squares[2][ai_index] = 2

        squareX = 2
        squareY = ai_index
    elif check_ai_row([squares[0][0], squares[1][0], squares[2][0]]):
        squares[ai_index][0] = 2

        squareX = ai_index
        squareY = 0
    elif check_ai_row([squares[0][1], squares[1][1], squares[2][1]]):
        squares[ai_index][1] = 2

        squareX = ai_index
        squareY = 1
    elif check_ai_row([squares[0][2], squares[1][2], squares[2][2]]):
        squares[ai_index][2] = 2

        squareX = ai_index
        squareY = 2
    elif check_ai_row([squares[0][0], squares[1][1], squares[2][2]]):
        squares[ai_index][ai_index] = 2

        squareX = ai_index
        squareY = ai_index
    elif check_ai_row([squares[0][2], squares[1][1], squares[2][0]]):
        squares[ai_index][2 - ai_index] = 2

        squareX = ai_index
        squareY = 2 - ai_index
    elif (squares[1][1] == 0):
        squares[1][1] = 2

        squareX = 1
        squareY = 1
    else:
        suitable_square = False

        while not suitable_square:
            row = random.choice([0, 1, 2])
            col = random.choice([0, 1, 2])

            if squares[0][1] == 0:
                squareX = 0
                squareY = 1

                suitable_square = True
                break
            elif squares[1][0] == 0:
                squareX = 1
                squareY = 0

                suitable_square = True
                break
            elif squares[2][1] == 0:
                squareX = 2
                squareY = 1

                suitable_square = True
                break
            elif squares[1][2] == 0:
                squareX = 1
                squareY = 2

                suitable_square = True
                break

            if squares[row][col] == 0 and not square[row].contains(1):
                squares[row][col] = 2

                squareX = row
                squareY = col

                suitable_square = True

    pointer.goto(squareX + 0.5, squareY + 0.5)
    pointer.shape("circle")
    pointer.shapesize(7)
    pointer.color("#eb8c34")
    pointer.stamp()

    pointer.shapesize(5)
    pointer.color("#ffffff")
    pointer.stamp()

    squares[squareX][squareY] = 2
    check_win()


def on_click(x, y):
    global player1Turn
    global squares
    global winner
    global current_buttons

    for button in current_buttons:
        if button.x1 < x < button.x2 and button.y1 < y < button.y2:
            button.on_click()
            current_buttons.remove(button)
            return

    if winner != 0:
        return

    if (x % 1 > 0.9 or x % 1 < 0.1) or (y % 1 > 0.9 or y % 1 < 0.1):
        return

    squareX = int(math.floor(x))
    squareY = int(math.floor(y))

    square = squares[squareX][squareY]

    if (square != 0):
        return

    pointer.goto(squareX + 0.5, squareY + 0.5)

    if player1Turn:
        draw_line(squareX + 0.25, squareY + 0.75, squareX + 0.75, squareY + 0.25, "#34ebe8", 15)
        draw_line(squareX + 0.25, squareY + 0.25, squareX + 0.75, squareY + 0.75, "#34ebe8", 15)

        player1Turn = False
        squares[squareX][squareY] = 1
    else:
        pointer.shape("circle")

        pointer.shapesize(7)
        pointer.color("#eb8c34")
        pointer.stamp()

        pointer.shapesize(5)
        pointer.color("#ffffff")
        pointer.stamp()

        player1Turn = True
        squares[squareX][squareY] = 2

    check_win()


def draw_main_menu():
    pointer.clear()

    pointer.goto(1.5, 2.5)
    pointer.color("red")
    pointer.write("TIC TAC TOE", True, align="center", font=("Comic Sans", 30, "bold"))

    draw_button(restart_1p, 1.1, 1.75, 1.475, 2.05, "1P", 1.2875, 1.84, 15, "white", "#09aedb", "#098edb", 0.05)
    draw_button(restart_2p, 1.525, 1.75, 1.9, 2.05, "2P", 1.7125, 1.84, 15, "white", "#e7f20f", "#dae329", 0.05)
    draw_button(load_game, 1.1, 1.4, 1.9, 1.7, "LOAD GAME", 1.5, 1.5, 15, "white", "#4ceb34", "#31c71a", 0.05)


def save_game():
    global squares

    with open('game.pkl', 'wb') as f:
        pickle.dump(squares, f)


def load_game():
    global squares

    restart_2p()

    with open('parrot.pkl', 'rb') as f:
        squares = pickle.load(f)

    for row in range(3):
        for box in range(3):
            pointer.goto(row + .5, box + .5)
            if squares[row][box] == 1:
                pass
            if squares[row][box] == 2:
                pointer.shape("circle")

                pointer.shapesize(7)
                pointer.color("#eb8c34")
                pointer.stamp()

                pointer.shapesize(5)
                pointer.color("#ffffff")
                pointer.stamp()


def restart_1p():
    screen.onclick(on_click_ai)
    restart()


def restart_2p():
    screen.onclick(on_click)
    restart()


def restart():
    global squares, winner, player1Turn

    pointer.clear()
    current_buttons.clear()

    pointer.pensize(5)

    draw_line(1, 0, 1, 3)
    draw_line(0, 2, 3, 2)
    draw_line(2, 3, 2, 0)
    draw_line(0, 1, 3, 1)

    squares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player1Turn = True
    winner = 0


winner = 0
player1Turn = True
ai_index = 0
squares = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

Button = namedtuple("Button", "x1 y1 x2 y2 on_click")
current_buttons = []

screen = turtle.Screen()
screen.screensize(700, 700)
screen.setworldcoordinates(0, 0, 3, 3)

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.up()
pointer.color("red")
pointer.speed(0)
pointer.pensize(5)

screen.onkey(save_game, "s")

draw_main_menu()

screen.onclick(on_click)
screen.listen()

screen.mainloop()