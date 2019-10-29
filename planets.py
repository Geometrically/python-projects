import math
import turtle

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def grav_mag(m1,x1,y1,m2,x2,y2):
    return m1*m2/distance(x1,y1,x2,y2)**2

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-5,-5,5,5)

t_step = .001

planet1 = Planet(1, Vector2(-3, 0), Vector2(0, .25), "red")
planet2 = Planet(1, Vector2(3, 0), Vector2(0, -.25), "green")

i=0

while True:
    f12 = grav_mag(planet1.mass, planet1.position.x, planet1.position.y, planet2.mass, planet2.position.x, planet2.position.y)
    
    planetMassOffset = planet1.mass - planet2.mass
    f12_theta = math.atan2(planetMassOffset.y, planetMassOffset.x)
   
    x1, y1 = vx1*t_step+x1, vy1*t_step+y1
    x2, y2 = vx2*t_step+x2, vy2*t_step+y2
   
    vx1, vy1 = f12*math.cos(f12_theta)/m1*t_step + vx1,f12*math.sin(f12_theta)/m1*t_step + vy1
    vx2, vy2 = f12*math.cos(f12_theta+math.pi)/m2*t_step + vx2,f12*math.sin(f12_theta+math.pi)/m2*t_step + vy2
   
    if i%1000 ==0:
        pointer1.goto(x1,y1)
        pointer2.goto(x2,y2)
        
    i+=1
    

class Planet:
    
    def __init__(self, mass, position, velocity, color):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        
        pointer = turtle.Turtle()
        self.pointer = pointer
        
        pointer = turtle.Turtle()
        pointer.up()
        pointer.shape("circle")
        pointer.color(color)
        pointer.speed(0)
        pointer.goto(position.x, position.y)
        pointer.down()
        
class Vector2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)
