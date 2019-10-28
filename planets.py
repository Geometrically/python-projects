import math
import turtle

gravity = 6.67430e-11

def Distance(x1, x2, y1, y2):
    offset1 = (x2 - x1)**2
    offset2 = (y2 - y1)**2
    
    return math.sqrt(offset1 + offset2)

def Gravity(mass1, x1, y1, mass2, x2, y2):
    return mass1 * mass2 * gravity / Distance(x1, y1, mass2, x2, y2)**2

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-5, -5, 5, 5)

mass1 = 1
mass2 = 1

x1, y1 = -3, 0
x2, y2 = 3, 0

vx1, vy1 = 0, .25
vx2, vy2 = 0, -.25


pointer2 = turtle.Turtle()
pointer2.up()
pointer2.shape("circle")
pointer2.color("green")
pointer2.speed(0)
pointer2.goto(x2, y2)
pointer2.down()

t_step = 0.1

while True:
    f12 = Gravity(mass1, x1, y1, mass2, x2, y2)
    f12_theta = math.atan2(y2 - y1, x2 - x1)
    
    x1,y1 = vx1*t_step + x1, vy1*t_step + y1
    x2,y2 = vx2*t_step + x2, vy2*t_step + y2

class Planet(object):
    
    def __init__(self, position, velocity, color):
        self.position = position
        self.velocity = velocity
                
        pointer = turtle.Turtle()
        self.pointer = pointer
        
        pointer.up()
        pointer.shape("circle")
        pointer.color(color)
        pointer.speed(0)
        pointer.goto(position.x, position.y)
        pointer.down()
        
    def SetVelocity(self, velocity):
        self.velocity = velocity
        
    def SetPosition(self, position):
        self.position = position
        
class Vector2(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
