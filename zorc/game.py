import turtle
import random
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
    draw_text(inv_pointer, "â†“ INVENTORY", 2.75, 2.45, 10, "black")

    for index, item in enumerate(items):
        draw_rect_text(inv_pointer, 2.5, 2.2 - index * 0.25, 2.9, 2.4 - index * 0.25, item, 2.7, 2.3 - index * 0.25, 10,
                       "white", "#e38412", "#a16216", 0.02)


def draw_actions(actions):
    actions_pointer.clear()
    draw_text(actions_pointer, "ACTIONS â†“", 0.15, 2.45, 10, "black")

    for index, action in enumerate(actions):
        draw_button(action.on_click, actions_pointer, 0.05, 2.2 - index * 0.25, 0.55, 2.4 - index * 0.25, action.name,
                    0.3, 2.3 - index * 0.25, 10, "white", "#e38412", "#a16216", 0.02)


def draw_lore_text(text):
    text_pointer.clear()
    
    if(len(text) > 46):
        draw_text(text_pointer, text[:46] + "-", 1.5, 0.35, 10, "white")
        draw_text(text_pointer, text[46:], 1.5, 0.3, 10, "white")
    else:
        draw_text(text_pointer, text, 1.5, 0.3, 10, "white")
    
    
def get_floor(x, y, z):
    for floor in floors:
        if floor.x == x and floor.y == y and floor.z == z:
            return floor
    
    return Floor(x, y, z, False, False, False, "none", False, "None", False)


def update_floor(floor, new_floor):
    global floors

    floors[floors.index(floor)] = new_floor
    init_floor(new_floor)

def win():
    draw_rect_text(board_pointer, 0.8, 1, 2.2, 2, "You won!", 1.5, 1.5)

    draw_button(restart, board_pointer, 1.1, 1.25, 1.45, 1.4, "RESTART", 1.275, 1.3125, 5, "white", "#09aedb", "#098edb", 0.01)
    draw_button(exit, board_pointer, 1.5, 1.25, 1.85, 1.4, "EXIT", 1.675, 1.3125, 5, "white", "#fc1303", "#db1c0f", 0.01)

def die():
    draw_rect_text(board_pointer, 0.8, 1, 2.2, 2, "You died!", 1.5, 1.5)

    draw_button(restart, board_pointer, 1.1, 1.25, 1.45, 1.4, "RESTART", 1.275, 1.3125, 5, "white", "#09aedb", "#098edb", 0.01)
    draw_button(exit, board_pointer, 1.5, 1.25, 1.85, 1.4, "EXIT", 1.675, 1.3125, 5, "white", "#fc1303", "#db1c0f", 0.01)

def restart():
    global floors
    global items
    
    floors = [
        Floor(1, 1, 1, False, False, False, "none", False, "Welcome to zorc! The king has sent you to retrieve the magic stone! Good Luck!", False), 
        Floor(0, 1, 2, False, False, False, "none", False, "What a useless room... Must be a dead end", False), 
        Floor(1, 1, 2, False, False, False, "none", False, "Left or right, what a dillema", False), 
        Floor(2, 1, 2, False, False, False, "sword", False, "That sword is shiny! It might be useful in the future for fighting.", False), 
        Floor(2, 1, 1, False, False, False, "none", False, "Oh no! A monster?? What will I do?", True), 
        Floor(3, 1, 2, False, True, False, "none", False, "A new level! This will get me closer to escaping", False),
        Floor(3, 2, 2, True, False, False, "none", False, "Very spooky... I hope I don't die", False),
        Floor(2, 2, 2, False, False, False, "sword", False, "Another sword, nice!", False),
        Floor(1, 2, 1, True, False, False, "none", False, "It looks like a one way hole.. No point of going down", False),
        Floor(1, 2, 2, False, False, False, "none", False, "A split choice, backward or forward, what will it be?", False),
        Floor(1, 2, 3, False, False, False, "none", False, "Oh no, a monster!", True),
        Floor(0, 2, 3, False, True, False, "none", False, "Yes! The next floor, I'm almost out of this place!", False),
        Floor(0, 3, 3, True, False, False, "none", False, "Something smells like trees here..", False),
        Floor(1, 3, 3, False, False, True, "none", False, "This stone might be useful in the future", False),
        Floor(1, 3, 2, False, False, False, "sword", False, "Yes, another sword!", False),
        Floor(2, 3, 2, False, False, False, "none", False, "Oh no, not another monster..", True),
        Floor(2, 3, 1, False, False, False, "potion", False, "I've never seen this potion before, it might be useful in the future!", False),
        Floor(3, 3, 2, False, False, False, "sword", False, "So many swords... I hope I don't have to use it soon", False),
        Floor(3, 3, 3, False, False, False, "none", True, "The boss! Once I beat this I can escape!", False)
    ]
    
    items = []
    
    draw_inv(items)

    
    init_floor(floors[0])
    
def init_floor(floor):
    global items
    global floors
    
    current_buttons.clear()

    available_actions = []

    board_pointer.clear()
    
    draw_lore_text(floor.enter_text)
    
    player.goto(1.5, 1.5)

    for other_floor in floors:
        if other_floor.x - floor.x == 1 and other_floor.y == floor.y and other_floor.z == floor.z:
            available_actions.append(Action("RIGHT", lambda: (
                player.goto(2.3, 1.5),
                init_floor(get_floor(floor.x + 1, floor.y, floor.z))
            )))
        elif other_floor.x - floor.x == -1 and other_floor.y == floor.y and other_floor.z == floor.z:
            available_actions.append(Action("LEFT", lambda: (
                player.goto(0.7, 1.5),
                init_floor(get_floor(floor.x - 1, floor.y, floor.z))
            )))
        
        if other_floor.z - floor.z == 1 and other_floor.y == floor.y and other_floor.x == floor.x:
            available_actions.append(Action("FORWARD", lambda: (
                player.goto(1.5, 2.0),
                init_floor(get_floor(floor.x, floor.y, floor.z + 1))
            )))
        elif other_floor.z - floor.z == -1 and other_floor.y == floor.y and other_floor.x == floor.x:
            available_actions.append(Action("BACKWARD", lambda: (
                player.goto(1.5, 0.7),
                init_floor(get_floor(floor.x, floor.y, floor.z - 1))
            )))        

    if floor.magic_stone:
        board_pointer.shape("stone.gif")
        board_pointer.goto(0.9, 0.7)
        board_pointer.stamp()

        available_actions.append(Action("GRAB STONE", lambda: (
            items.append("Magic Stone"),
            draw_inv(),
            player.goto(0.9, 0.7),
            update_floor(floor, Floor(floor.x, floor.y, floor.z, floor.down_staircase, floor.up_staircase, False, floor.item, floor.has_boss, floor.enter_text, False))
        )))
    if floor.down_staircase:
        board_pointer.shape("manhole.gif")
        board_pointer.goto(1.0, 2.2)
        board_pointer.stamp()

        available_actions.append(Action("DOWN", lambda: (
            player.goto(1.0, 2.2),
            init_floor(get_floor(floor.x, floor.y - 1, floor.z))
        )))
    if floor.up_staircase:
        board_pointer.shapesize(1, 1)
        board_pointer.shape("ladder.gif")
        board_pointer.goto(2.0, 2.1)
        board_pointer.stamp()

        available_actions.append(Action("UP", lambda: (
            player.goto(2.0, 2.1),
            init_floor(get_floor(floor.x, floor.y + 1, floor.z))
        )))
    if floor.item != "none":
        draw_text(board_pointer, floor.item, 1.5, 0.7, 10, "black")

        available_actions.append(Action("GRAB " + floor.item, lambda: (
            items.append(floor.item),
            draw_inv(),
            player.goto(1.5, 0.7),
            update_floor(floor, Floor(floor.x, floor.y, floor.z, floor.down_staircase, floor.up_staircase, floor.magic_stone, "none", floor.has_boss, "I've already been here...", False))
        )))
    if floor.monster:
        board_pointer.shape("monster.gif")
        board_pointer.goto(1.0, 1.5)
        board_pointer.stamp()
        
        old_action = available_actions[0]
        available_actions.clear()
        available_actions.append(Action("RUN", old_action.on_click))
        
        player.goto(2.0, 1.5)
        
        if "sword" in items:
            available_actions.append(Action("KILL MONSTER", lambda: (
                items.remove("sword"),
                draw_inv(),
                player.goto(1.5, 1.5),
                update_floor(floor, Floor(floor.x, floor.y, floor.z, floor.down_staircase, floor.up_staircase, floor.magic_stone, floor.item, floor.has_boss, "I've already been here", False))
            )))
        else:
            available_actions.append(Action("KILL MONSTER", die))
           
    if floor.has_boss:
        board_pointer.shape("boss.gif")
        board_pointer.goto(1.0, 1.5)
        board_pointer.stamp()
        
        player.goto(2.0, 1.5)
        
        if "sword" in items and "magic_stone" in items and "potion" in items and random.randint(0,100) <= 40:
            available_actions.append(Action("KILL BOSS", win))
        else:
            available_actions.append(Action("KILL BOSS", die))
        
    draw_actions(available_actions)

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

Floor = namedtuple("Floor", "x y z down_staircase up_staircase magic_stone item has_boss enter_text monster")
floors = [
    Floor(1, 1, 1, False, False, False, "none", False, "Welcome to zorc! The king has sent you to retrieve the magic stone! Good Luck!", False), 
    Floor(0, 1, 2, False, False, False, "none", False, "What a useless room... Must be a dead end", False), 
    Floor(1, 1, 2, False, False, False, "none", False, "Left or right, what a dillema", False), 
    Floor(2, 1, 1, False, False, False, "sword", False, "That sword is shiny! It might be useful in the future for fighting.", False), 
    Floor(2, 1, 2, False, False, False, "none", False, "Oh no! A monster?? What will I do?", True), 
    Floor(3, 1, 2, False, True, False, "none", False, "A new level! This will get me closer to escaping", False),
    Floor(3, 2, 2, True, False, False, "none", False, "Very spooky... I hope I don't die", False),
    Floor(2, 2, 2, False, False, False, "sword", False, "Another sword, nice!", False),
    Floor(1, 2, 1, True, False, False, "none", False, "It looks like a one way hole.. No point of going down", False),
    Floor(1, 2, 2, False, False, False, "none", False, "A split choice, backward or forward, what will it be?", False),
    Floor(1, 2, 3, False, False, False, "none", False, "Oh no, a monster!", True),
    Floor(0, 2, 3, False, True, False, "none", False, "Yes! The next floor, I'm almost out of this place!", False),
    Floor(0, 3, 3, True, False, False, "none", False, "Something smells like trees here..", False),
    Floor(1, 3, 3, False, False, True, "none", False, "This stone might be useful in the future", False),
    Floor(1, 3, 2, False, False, False, "sword", False, "Yes, another sword!", False),
    Floor(2, 3, 2, False, False, False, "none", False, "Oh no, not another monster..", True),
    Floor(2, 3, 1, False, False, False, "potion", False, "I've never seen this potion before, it might be useful in the future!", False),
    Floor(3, 3, 2, False, False, False, "sword", False, "So many swords... I hope I don't have to use it soon", False),
    Floor(3, 3, 3, False, False, False, "none", True, "The boss! Once I beat this I can escape!", False)
]

items = []

screen = turtle.Screen()
screen.screensize(700, 700)
screen.setworldcoordinates(0, 0, 3, 3)

screen.register_shape('link.gif')
screen.register_shape('ladder.gif')
screen.register_shape('manhole.gif')
screen.register_shape('monster.gif')
screen.register_shape('stone.gif')
screen.register_shape('boss.gif')

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

text_pointer = turtle.Turtle()
text_pointer.hideturtle()
text_pointer.up()
text_pointer.speed(0)
text_pointer.pensize(5)

draw_text(fixed_pointer, "ZORK by Jai", 1.5, 2.6, 30, "black")
draw_rect(fixed_pointer, 0.6, 0.5, 2.4, 2.5, "white", "#6e410a", 0.05)

draw_rect(fixed_pointer, 0.6, 0.27, 2.4, 0.48, "#a35718", "#733f14", 0.02)

draw_button(exit, fixed_pointer, 0.6, 0.05, 2.4, 0.25, "EXIT", 1.5, 0.14, 10, "white", "#f71121", "#d11320", 0.05)

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
