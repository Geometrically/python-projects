import turtle
import math
import random
import pickle
from collections import namedtuple

def draw_rect_text(x1, y1, x2, y2, text, textX, textY, text_size=20, text_color ="white", color="#0cf54a", border_color ="#09db41", border_size = 0.05):
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

    draw_text(text, textX, textY, text_size, text_color)

def draw_text(text, textX, textY, text_size=20, text_color ="white"):
    pointer.color(text_color)
    pointer.goto(textX, textY)
    pointer.write(text, True, align="center", font=("Courier", text_size, "bold"))

def draw_rect(x1, y1, x2, y2, color="#0cf54a", border_color ="#09db41", border_size = 0.05):
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

def draw_button(button_callback, x1, y1, x2, y2, text, textX, textY, text_size=20, text_color ="white", color="#0cf54a", border_color ="#09db41", border_size = 0.05):
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

Button = namedtuple("Button", "x1 y1 x2 y2 on_click")
current_buttons = []

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(0, 0, 3, 3)

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.up()
pointer.speed(0)
pointer.pensize(5)

screen.listen()

draw_text("ZORC by Jai", 1.5, 2.6, 30, "black")
draw_rect(0.6, 0.5, 2.4, 2.5, "white", "#6e410a", 0.05)

draw_rect_text(0.6, 0.3, 1.15, 0.45, "HELP", 0, 0, 0, "white", "#4287f5", "#2253a1", 0.05)
draw_rect_text(1.25, 0.3, 2.4, 0.45, "EXIT", 0, 0, 0, "white", "#f71121", "#d11320", 0.05)

draw_text("ACTIONS ↓", 0.15, 2.45, 10, "black")
draw_rect_text(0.1, 2.2, 0.5, 2.4,"TEST", 0.3, 2.26, 10, "white", "#e38412", "#a16216", 0.02)

draw_text("↓ INVENTORY", 2.75, 2.45, 10, "black")
draw_rect_text(2.5, 2.2, 2.9, 2.4,"TEST", 2.7, 2.26, 10, "white", "#e38412", "#a16216", 0.02)

screen.mainloop()
