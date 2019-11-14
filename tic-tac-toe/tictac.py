import turtle
import math

def draw_line(x1, y1, x2, y2):
    pointer.up()
    pointer.goto(x1, y1)
    pointer.down()
    pointer.goto(x2, y2)
    pointer.up()

def check_win():
    global squares
    
    for row in squares:
        if len(set(row)) <= 1:
            print("win")
            return True

def box_clicker(x, y):
    global player1Turn
    global squares
        
    if (x % 1 > 0.9 or x % 1 < 0.1) or (y % 1 > 0.9 or y % 1 < 0.1):
        return
    
    squareX = int(math.floor(x))
    squareY = int(math.floor(y))
    
    square = squares[squareX][squareY]
        
    if(square == 0):
        pointer.goto(squareX + 0.5, squareY + 0.5)
    
    if player1Turn:
        pointer.shape("circle")
        player1Turn = False
        square = 1
    else:
        pointer.shape("turtle")
        player1Turn = True
        square = 2
    
    pointer.stamp()
    check_win()
    
def clear():
    pointer.clearstamps()


player1Turn = True
squares = [[0,0,0], [0,0,0], [0,0,0]]

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(0, 0, 3, 3)

pointer = turtle.Turtle()
pointer.shape("turtle")
pointer.hideturtle()
pointer.up()
pointer.color("red")
pointer.speed(0)
pointer.shapesize(3, 3)
pointer.pensize(15)

draw_line(1, -1, 1, 3)
draw_line(-1, 2, 3, 2)
draw_line(2, 3, 2, -1)
draw_line(-1, 1, 3, 1)

screen.onclick(box_clicker)
screen.onkey(clear, "c")

screen.listen()

screen.mainloop()
