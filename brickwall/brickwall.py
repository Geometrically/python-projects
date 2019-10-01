import turtle

screen = turtle.Screen()
screen.screensize(400, 400)
screen.setworldcoordinates(0, 0, 400, 400)

pointer = turtle.Turtle()
pointer.up()
pointer.hideturtle()
pointer.speed(0)


def drawRect(x, y, length, height):
    pointer.up()
    pointer.goto(x, y)
    pointer.begin_fill()
    pointer.down()
    pointer.goto(x + length, y)
    pointer.goto(x + length, y + height)
    pointer.goto(x, y + height)
    pointer.goto(x, y)
    pointer.up()
    pointer.end_fill()


def drawBrickWallOffset(rows, cols, brickWidth, brickHeight, mortarWidth):
    for row in range(rows):
        for column in range(cols):
            x = row * brickWidth + row * mortarWidth
            y = column * brickHeight + column * mortarWidth

            if column % 2:
                if row == 0 or row == (rows - 1):
                    drawRect(x + brickWidth/2 - brickWidth - mortarWidth/2, y, brickWidth, brickHeight)
                else:
                    drawRect(x + brickWidth/2 - brickWidth - mortarWidth/2, y, brickWidth, brickHeight)
            else:
                drawRect(x, y, brickWidth, brickHeight)


def drawBrickWall(rows, cols, brickWidth, brickHeight, mortarWidth):
    for row in range(rows):
        for column in range(cols):
            x = row * brickWidth + row * mortarWidth
            y = column * brickHeight + column * mortarWidth

            drawRect(x, y, brickWidth, brickHeight)


drawBrickWallOffset(4, 3, 50, 25, 8)
turtle.done()
