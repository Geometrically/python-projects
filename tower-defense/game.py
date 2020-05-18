import turtle
from collections import namedtuple

def on_click(x, y):
    global current_buttons

    for button in current_buttons:
        if button.x1 < x < button.x2 and button.y1 < y < button.y2:
            button.on_click()
            current_buttons.remove(button)
            return

screen = turtle.Screen()
screen.screensize(700, 700)
screen.setworldcoordinates(0, 0, 3, 3)

Button = namedtuple("Button", "x1 y1 x2 y2 on_click")
current_buttons = []

screen.onclick(on_click)
screen.listen()
screen.mainloop()
