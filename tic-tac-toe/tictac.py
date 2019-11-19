import turtle
import math
from Tools.demo.ss1 import center

def draw_rect(x1, y1, x2, y2, text, text_size, text_color ="white", color="#fc5203", border_color ="#03fc13", border_size = 100):
    pointer.fillcolor(color)
    pointer.color(border_color)
    pointer.pensize(border_size)
    
    pointer.begin_fill()
    
    pointer.goto(x1, y1)
    pointer.down()

    pointer.goto(x2, y1)
    pointer.goto(x2, y2)
    pointer.goto(x1, y2)
    pointer.goto(x1, y1)
    
    pointer.end_fill()
    pointer.up()
    
    pointer.color(text_color)
    pointer.goto((x1 + x2)/2, (y1 + y2)/2)
    pointer.write(text, True, align="center", font=("Comic Sans", text_size, "bold"))

def draw_line(x1, y1, x2, y2, color="#636E72", pensize=5):
    pointer.pensize(pensize)
    pointer.color(color)
    pointer.up()
    pointer.goto(x1, y1)
    pointer.down()
    pointer.goto(x2, y2)
    pointer.up()

def check_win_row(win_rows):
    return win_rows[0] != 0 and win_rows.count(win_rows[0]) == len(win_rows)

def check_win():
    global squares
    
    if ( 
        check_win_row(squares[0]) or check_win_row(squares[1]) or check_win_row(squares[2]) or
        check_win_row([squares[0][0], squares[1][0], squares[2][0]]) or
        check_win_row([squares[0][1], squares[1][1], squares[2][1]]) or
        check_win_row([squares[0][2], squares[1][2], squares[2][2]]) or
        check_win_row([squares[0][0], squares[1][1], squares[2][2]]) or
        check_win_row([squares[0][2], squares[1][1], squares[2][0]])):
        
        draw_rect(1, 1.25, 2, 1.75, "YOU WIN!", 20)
        
def box_clicker(x, y):
    global player1Turn
    global squares
        
    if (x % 1 > 0.9 or x % 1 < 0.1) or (y % 1 > 0.9 or y % 1 < 0.1):
        return
        
    squareX = int(math.floor(x))
    squareY = int(math.floor(y))
    
    square = squares[squareX][squareY]
        
    if(square != 0):
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
        pointer.color("white")
        pointer.stamp()
                
        player1Turn = True
        squares[squareX][squareY] = 2

    check_win()
    
def clear():
    pointer.clearstamps()


player1Turn = True
squares = [[0,0,0], [0,0,0], [0,0,0]]

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(0, 0, 3, 3)

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.up()
pointer.color("red")
pointer.speed(0)
pointer.pensize(5)

draw_line(1, -1, 1, 3)
draw_line(-1, 2, 3, 2)
draw_line(2, 3, 2, -1)
draw_line(-1, 1, 3, 1)

screen.onclick(box_clicker)
screen.onkey(clear, "c")

screen.listen()

screen.mainloop()
