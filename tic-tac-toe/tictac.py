import turtle
import math

def draw_line(x1, y1, x2, y2):
    pointer.color("red")

    pointer.up()
    pointer.goto(x1, y1)
    pointer.down()
    pointer.goto(x2, y2)
    pointer.up()

def check_win():
    global squares
    
    win = False
    
    for row in squares:
        for box in row:
            if box == 0:
                win = False
                break
            win = True
        if win:
            win = row.count(row[0]) == len(row)
            
            if win:
                break
    
    for column in zip(*matrix): 
    
    print(win)
    
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
        draw_line(squareX + 0.25, squareY + 0.75, squareX + 0.75, squareY + 0.25)
        draw_line(squareX + 0.25, squareY + 0.25, squareX + 0.75, squareY + 0.75)

        player1Turn = False
        squares[squareX][squareY] = 1
    else:
        pointer.shape("circle")
        
        pointer.shapesize(7)
        pointer.color("red")
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
pointer.pensize(15)

draw_line(1, -1, 1, 3)
draw_line(-1, 2, 3, 2)
draw_line(2, 3, 2, -1)
draw_line(-1, 1, 3, 1)

screen.onclick(box_clicker)
screen.onkey(clear, "c")

screen.listen()

screen.mainloop()
