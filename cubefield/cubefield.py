import turtle
from collections import namedtuple
import random
import math
import asyncturtle
import asyncio
import gc


def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def move_left():
    global moving_left = True

  


def stop_move_left():
    global moving_left = False

    
def move_right():
    global moving_right = True



def stop_move_right():
    global moving_right = False

    


def on_click(x, y):
    global current_buttons

    for button in current_buttons:
        if button.x1 < x < button.x2 and button.y1 < y < button.y2:
            button.on_click()
            current_buttons.remove(button)
            return 


def restart():
    global game_over, score

    player.clear()
    player.goto(250, 100)
    player.showturtle()

    for enemy in current_enemies:
        enemy.hideturtle()
        current_enemies.remove(enemy)

    score = 0
    game_over = False

    screen.ontimer(update_screen, 1)


def update_screen():
    global game_over, score

    if game_over:
        return

    score += 1
    scoreWriter.clear()
    scoreWriter.write(score, align="center", font=("Arial", 20, "normal"))

    tasks = []

    if score % 5 == 0:
        x_pos = random.randint(0, 500)

        square = asyncturtle.AsyncTurtle()

        square.shape("square")
        square.up()
        square.shapesize(0.1)
        square.hideturtle()
        square.color((252 - score // 5) % 255, (186 - score // 5) % 255, (3 + score // 5) % 255)
        square.speed(0)
        tasks.append(square.goto(x_pos, 250))
        square.showturtle()
        tasks.append(square.setheading(270))
        square.goto(x_pos, -1)

        current_enemies.append(square)

    for current_enemy in current_enemies:
        if distance(current_enemy.xcor(), player.xcor(), current_enemy.ycor(), player.ycor()) < 20:
            game_over = True
            player.goto(250, 250)
            player.hideturtle()
            player.write("Game Over!", align="center", font=("Arial", 20, "normal"))
            player.goto(250, 200)
            player.write("Press 'r' to restart!", align="center", font=("Arial", 20, "normal"))
            screen.onkey(restart, "r")
        else:
            if current_enemy.ycor() < 0:
                current_enemies.remove(current_enemy)
                current_enemy.hideturtle()
                del current_enemy
                gc.collect()
            else:
                tasks.append(current_enemy.forward(1 + score // 50))
                current_enemy.shapesize(0.5 + (250 - current_enemy.ycor()) * 2 / 250)

    tasks += [enemy.forward(10) for enemy in current_enemies]

    if len(tasks) > 0:
        loop.run_until_complete(asyncio.wait(tasks))

    if moving_left and player.xcor() > 0:
        player.setheading(180)
        player.forward(10)

    if moving_right and player.xcor() < 500:
        player.setheading(0)
        player.forward(10)

    if not game_over:
        screen.ontimer(update_screen, 1)


screen = turtle.Screen()
screen.screensize(700, 700)
screen.setworldcoordinates(0, 0, 500, 500)

Button = namedtuple("Button", "x1 y1 x2 y2 on_click")
current_buttons = []

current_enemies = []

moving_left = False
moving_right = False

game_over = False

score = 0

loop = asyncio.get_event_loop()

player = turtle.Turtle()

player.shape("triangle")
player.up()
player.shapesize(1)
player.speed(0)
player.goto(250, 100)
player.speed(0)
player.setheading(90)

horizon = turtle.Turtle()
horizon.hideturtle()
horizon.speed(0)
horizon.up()
horizon.goto(0, 250)
horizon.down()
horizon.goto(500, 250)
horizon.up()
horizon.goto(250, 450)

scoreWriter = turtle.Turtle()
scoreWriter.hideturtle()
scoreWriter.speed(0)
scoreWriter.goto(250, 450)

screen.onclick(on_click)
screen.onkeypress(move_left, "a")
screen.onkeyrelease(stop_move_left, "a")

screen.onkeypress(move_right, "d")
screen.onkeyrelease(stop_move_right, "d")

screen.colormode(255)

screen.listen()

screen.ontimer(update_screen, 1)

screen.mainloop()
