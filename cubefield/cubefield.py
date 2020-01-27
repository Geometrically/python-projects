import turtle
from collections import namedtuple
import random
import math

def distance(a, b):
    if (a == b):
        return 0
    elif (a < 0) and (b < 0) or (a > 0) and (b > 0):
        if (a < b):
            return (abs(abs(a) - abs(b)))
        else:
            return -(abs(abs(a) - abs(b)))
    else:
        return math.copysign((abs(a) + abs(b)),b)


def move_left():
    global moving_left
    
    moving_left = True        

def stop_move_left():
    global moving_left
    
    moving_left = False

def move_right():
    global moving_right
    
    moving_right = True        

def stop_move_right():
    global moving_right
    
    moving_right = False

def spawn_square():
    global current_enemies
    
    xPos = random.randint(100, 400)
    
    square = turtle.Turtle()
    
    square.shape("square")
    square.up()
    square.shapesize(1, 1)
    square.color("orange")
    square.hideturtle()
    square.speed(0)
    square.goto(xPos, 400)
    square.showturtle()
    square.setheading(270)
    
    current_enemies.append(square)
    
def on_click(x, y):
    global current_buttons

    for button in current_buttons:
        if button.x1 < x < button.x2 and button.y1 < y < button.y2:
            button.on_click()
            current_buttons.remove(button)
            return

def spawn_enemy():
    spawn_square()
    screen.ontimer(spawn_enemy, random.randint(600, 900))

def update_screen():
    for current_enemy in current_enemies: 
        current_enemy.forward(10)
    
    if moving_left:
        player.setheading(180)
        player.forward(10)
    
    if moving_right:
        player.setheading(0)
        player.forward(10)
        
        
    screen.ontimer(update_screen, 5)

screen = turtle.Screen()
screen.screensize(700, 700)
screen.setworldcoordinates(0, 0, 500, 500)

Button = namedtuple("Button", "x1 y1 x2 y2 on_click")
current_buttons = []    

current_enemies = []

moving_left = False
moving_right = False

player = turtle.Turtle()

player.shape("triangle")
player.up()
player.shapesize(3, 3)
player.speed(0)
player.goto(250, 100)
player.speed(0)
player.setheading(90)

screen.onclick(on_click)

screen.onkeypress(move_left, "a")
screen.onkeyrelease(stop_move_left, "a")

screen.onkeypress(move_right, "d")
screen.onkeyrelease(stop_move_right, "d")
    
screen.listen()

screen.ontimer(spawn_enemy, 1)
screen.ontimer(update_screen, 5)

screen.mainloop()
