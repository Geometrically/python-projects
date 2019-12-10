import turtle
from collections import namedtuple

def draw_rect_text(pointer, x1, y1, x2, y2, text, textX, textY, text_size=20, text_color ="white", color="#0cf54a", border_color ="#09db41", border_size = 0.05):
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

    draw_text(pointer, text, textX, textY, text_size, text_color)

def draw_text(pointer, text, textX, textY, text_size=20, text_color ="white"):
    pointer.color(text_color)
    pointer.goto(textX, textY)
    pointer.write(text, True, align="center", font=("Courier", text_size, "bold"))

def draw_rect(pointer, x1, y1, x2, y2, color="#0cf54a", border_color ="#09db41", border_size = 0.05):
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

def draw_button(button_callback, pointer, x1, y1, x2, y2, text, textX, textY, text_size=20, text_color ="white", color="#0cf54a", border_color ="#09db41", border_size = 0.05):
    draw_rect(pointer, x1, y1, x2, y2, text, textX, textY, text_size, text_color, color, border_color, border_size)
    current_buttons.append(Button(x1, y1, x2, y2, button_callback))
    
def draw_line(pointer, x1, y1, x2, y2, color="#636E72", pensize=5):
    pointer.pensize(pensize)
    pointer.color(color)
    pointer.up()
    pointer.goto(x1, y1)
    pointer.down()
    pointer.goto(x2, y2)
    pointer.up()
    
def draw_inv(pointer, actions):
    pointer.clear()
    draw_text(pointer, "↓ INVENTORY", 2.75, 2.45, 10, "black")
    
    for index, action in enumerate(actions):
        draw_rect_text(pointer, 2.5, 2.2 - index*0.25, 2.9, 2.4 - index*0.25,"TEST", 2.7, 2.26 - index*0.25, 10, "white", "#e38412", "#a16216", 0.02)
        
def draw_actions(pointer, actions):
    pointer.clear()
    draw_text(pointer, "ACTIONS ↓", 0.15, 2.45, 10, "black")
    
    for index, action in enumerate(actions):
        draw_rect_text(pointer, 0.1, 2.2 - index*0.25, 0.5, 2.4 - index*0.25, action, 0.3, 2.26 - index*0.25, 10, "white", "#e38412", "#a16216", 0.02)

def draw_floor(floor):
    pass

Button = namedtuple("Button", "x1 y1 x2 y2 on_click")
current_buttons = []

Floor = namedtuple("Floor", "x y down_staircase up_staircase magic_stone item")

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(0, 0, 3, 3)

screen.register_shape('zelda.gif')

fixed_pointer = turtle.Turtle()
fixed_pointer.hideturtle()
fixed_pointer.up()
fixed_pointer.speed(0)
fixed_pointer.pensize(5)

actions_pointer = turtle.Turtle()
actions_pointer.hideturtle()
actions_pointer.up()
actions_pointer.speed(0)
actions_pointer.pensize(5)

inv_pointer = turtle.Turtle()
inv_pointer.hideturtle()
inv_pointer.up()
inv_pointer.speed(0)
inv_pointer.pensize(5)

screen.listen()

draw_text(fixed_pointer, "ZORC by Jai", 1.5, 2.6, 30, "black")
draw_rect(fixed_pointer, 0.6, 0.5, 2.4, 2.5, "white", "#6e410a", 0.05)

draw_rect_text(fixed_pointer, 0.6, 0.25, 1.45, 0.45, "HELP", 1.025, 0.3, 10, "white", "#4287f5", "#2253a1", 0.05)
draw_rect_text(fixed_pointer, 1.55, 0.25, 2.4, 0.45, "EXIT", 1.975, 0.3, 10, "white", "#f71121", "#d11320", 0.05)

draw_actions(actions_pointer, ["Ts", "tets"])
draw_inv(inv_pointer, ["sword", "apple"])

player = turtle.Turtle()
player.shape("zelda.gif")
player.up()
player.shapesize(1)
player.goto(1.5, 1.5)

screen.mainloop()
