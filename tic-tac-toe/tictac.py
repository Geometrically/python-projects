import turtle

def draw_line(x1, y1, x2, y2):
    pointer.up()
    pointer.goto(x1, y1)
    pointer.down()
    pointer.goto(x2, y2)
    pointer.up()

def box_clicker(x, y):
    if 1.1 < x < 1.9 and 1.1<y<1.9:
        pointer.goto(1.5, 1.5)
        pointer.stamp()
    
def clear():
    pointer.clearstamps()

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(0, 0, 3, 3)

pointer = turtle.Turtle()
pointer.shape("turtle")
pointer.hideturtle()
pointer.up()
pointer.color("red")
pointer.speed(0)
pointer.pensize(15)

draw_line(1, 1, 1, 2)
draw_line(1, 2, 2, 2)
draw_line(2, 2, 2, 1)
draw_line(2, 1, 1, 1)

screen.onclick(box_clicker)
screen.onkey(clear, "c")

screen.listen()

screen.mainloop()
