import turtle
import time
from collections import namedtuple


def draw_rect_text(pointer, x1, y1, x2, y2, text, text_x, text_y, text_size=20, text_color="white", color="#0cf54a",
                   border_color="#09db41", border_size=0.05):
    draw_rect(pointer, x1, y1, x2, y2, color, border_color, border_size)
    draw_text(pointer, text, text_x, text_y, text_size, text_color)


def draw_text(pointer, text, textX, textY, text_size=20, text_color="white"):
    pointer.color(text_color)
    pointer.goto(textX, textY)
    pointer.write(text, True, align="center", font=("Courier", text_size, "bold"))


def draw_rect(pointer, x1, y1, x2, y2, color="#0cf54a", border_color="#09db41", border_size=0.05):
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


def draw_button(button_callback, pointer, x1, y1, x2, y2, text, text_x, text_y, text_size=20, text_color="white",
                color="#0cf54a", border_color="#09db41", border_size=0.05):
    draw_rect_text(pointer, x1, y1, x2, y2, text, text_x, text_y, text_size, text_color, color, border_color,
                   border_size)
    current_buttons.append(Button(x1, y1, x2, y2, button_callback))


def draw_line(pointer, x1, y1, x2, y2, color="#636E72", pensize=5):
    pointer.pensize(pensize)
    pointer.color(color)
    pointer.up()
    pointer.goto(x1, y1)
    pointer.down()
    pointer.goto(x2, y2)
    pointer.up()


def draw_inv():
    inv_pointer.clear()
    draw_text(inv_pointer, "↓ INVENTORY", 2.75, 2.45, 10, "black")

    for index, item in enumerate(items):
        draw_rect_text(inv_pointer, 2.5, 2.2 - index * 0.25, 2.9, 2.4 - index * 0.25, item, 2.7, 2.3 - index * 0.25, 10,
                       "white", "#e38412", "#a16216", 0.02)


def draw_actions(actions):
    actions_pointer.clear()
    draw_text(actions_pointer, "ACTIONS ↓", 0.15, 2.45, 10, "black")

    for index, action in enumerate(actions):
        draw_button(action.on_click, actions_pointer, 0.05, 2.2 - index * 0.25, 0.55, 2.4 - index * 0.25, action.name,
                    0.3, 2.3 - index * 0.25, 10, "white", "#e38412", "#a16216", 0.02)


def get_floor(x, y):
    horizontal_floors = []

    for floor in floors:
        if floor.x == x:
            horizontal_floors.append(floor)

    for horizontal_floor in horizontal_floors:
        if horizontal_floor.y == y:
            return horizontal_floor

    return Floor(x, y, False, False, False, "none", False)


def update_floor(floor, new_floor):
    global floors

    floors[floors.index(floor)] = new_floor


def init_floor(floor):
    global items
    global floors

    available_actions = []

    draw_rect(transition_pointer, 0.65, 0.55, 2.35, 2.45, "#676269", "#ffffff", 0)
    time.sleep(.400)
    draw_rect(transition_pointer, 0.65, 0.55, 2.35, 2.45, "#514f52", "#ffffff", 0)
    time.sleep(.400)
    draw_rect(transition_pointer, 0.65, 0.55, 2.35, 2.45, "#000000", "#ffffff", 0)

    board_pointer.clear()
    player.goto(1.5, 1.5)

    for other_floor in floors:
        if other_floor.x - floor.x == 1 and other_floor.y == floor.y:
            available_actions.append(Action("RIGHT", lambda: (
                player.goto(2.3, 1.5),
                init_floor(get_floor(floor.x + 1, floor.y))
            )))
            break
        elif other_floor.x - floor.x == -1 and other_floor.y == floor.y:
            available_actions.append(Action("LEFT", lambda: (
                player.goto(0.7, 1.5),
                init_floor(get_floor(floor.x - 1, floor.y))
            )))
            break

    if floor.magic_stone:
        board_pointer.shape("stone.gif")
        board_pointer.goto(0.9, 0.7)
        board_pointer.stamp()

        available_actions.append(Action("GRAB STONE", lambda: (
            items.append("Magic Stone"),
            draw_inv(),
            player.goto(0.9, 0.7),
            update_floor(floor, Floor(floor.x, floor.y, floor.down_staircase, floor.up_staircase, False, floor.item, floor.has_boss))
        )))
    if floor.down_staircase:
        board_pointer.shape("manhole.gif")
        board_pointer.goto(1.0, 2.2)
        board_pointer.stamp()

        available_actions.append(Action("DOWN", lambda: (
            player.goto(1.0, 2.2),
            init_floor(get_floor(floor.x, floor.y - 1))
        )))
    if floor.up_staircase:
        board_pointer.shapesize(1, 1)
        board_pointer.shape("ladder.gif")
        board_pointer.goto(2.0, 2.1)
        board_pointer.stamp()

        available_actions.append(Action("UP", lambda: (
            player.goto(2.0, 2.1),
            init_floor(get_floor(floor.x, floor.y + 1))
        )))
    if floor.item != "none":
        draw_text(board_pointer, floor.item, 1.5, 0.7, 10, "black")

        available_actions.append(Action("GRAB " + floor.item, lambda: (
            items.append(floor.item),
            draw_inv(),
            player.goto(1.5, 0.7),
            update_floor(floor, Floor(floor.x, floor.y, floor.down_staircase, floor.up_staircase, floor.magic_stone, "none", floor.has_boss))
        )))


    draw_actions(available_actions)

    draw_rect(transition_pointer, 0.65, 0.55, 2.35, 2.45, "#514f52", "#ffffff", 0)
    time.sleep(.400)
    draw_rect(transition_pointer, 0.65, 0.55, 2.35, 2.45, "#676269", "#ffffff", 0)
    time.sleep(.400)
    draw_rect(transition_pointer, 0.65, 0.55, 2.35, 2.45, "#000000", "#ffffff", 0)
    transition_pointer.clear()



def on_click(x, y):
    global current_buttons

    for button in current_buttons:
        if button.x1 < x < button.x2 and button.y1 < y < button.y2:
            button.on_click()
            current_buttons.remove(button)
            return


Action = namedtuple("Action", "name on_click")

Button = namedtuple("Button", "x1 y1 x2 y2 on_click")
current_buttons = []

Floor = namedtuple("Floor", "x y down_staircase up_staircase magic_stone item has_boss")
floors = [Floor(1, 1, True, True, False, "sdesd", False), Floor(0, 1, False, True, False, "sdesd", False)]

items = []

screen = turtle.Screen()
screen.screensize(700, 700)
screen.setworldcoordinates(0, 0, 3, 3)

screen.register_shape('link.gif')
screen.register_shape('ladder.gif')
screen.register_shape('manhole.gif')
screen.register_shape('monster.gif')
screen.register_shape('stone.gif')

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

board_pointer = turtle.Turtle()
board_pointer.hideturtle()
board_pointer.up()
board_pointer.speed(0)
board_pointer.pensize(5)

transition_pointer = turtle.Turtle()
transition_pointer.hideturtle()
transition_pointer.up()
transition_pointer.speed(0)
transition_pointer.pensize(5)

draw_text(fixed_pointer, "ZORC by Jai", 1.5, 2.6, 30, "black")
draw_rect(fixed_pointer, 0.6, 0.5, 2.4, 2.5, "white", "#6e410a", 0.05)

draw_rect_text(fixed_pointer, 0.6, 0.25, 1.45, 0.45, "HELP", 1.025, 0.32, 10, "white", "#4287f5", "#2253a1", 0.05)
draw_rect_text(fixed_pointer, 1.55, 0.25, 2.4, 0.45, "EXIT", 1.975, 0.32, 10, "white", "#f71121", "#d11320", 0.05)

player = turtle.Turtle()
player.shape("link.gif")
player.up()
player.shapesize(1)
player.speed(0)
player.goto(1.5, 1.5)
player.speed(2)

init_floor(floors[0])

screen.onclick(on_click)
screen.listen()
screen.mainloop()
