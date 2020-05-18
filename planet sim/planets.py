import math
import turtle
import util


def distance(pointA, pointB):
    return math.sqrt((pointB.x-pointA.x)**2 + (pointB.y-pointA.y)**2)

def grav_mag(planetA, planetB):
    return planetA.mass*planetB.mass/distance(planetA.position, planetB.position)**2

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-5,-5,5,5)

t_step = .001

planet3 = util.Planet(1, util.Vector2(0, 0), util.Vector2(-0.93240737, -0.86473146), "green")
planet1 = util.Planet(1, util.Vector2(0.97000436, -0.24308753), util.Vector2(-planet3.velocity.x / 2, -planet3.velocity.y / 2), "red")
planet2 = util.Planet(1, util.Vector2(-planet1.position.x, -planet1.position.y), planet1.velocity, "blue")

i=0

while True:
    f12 = grav_mag(planet1, planet2)
    f23 = grav_mag(planet2, planet3)
    f13 = grav_mag(planet1, planet3)

    planet12PosOffset = planet2.position - planet1.position
    planet23PosOffset = planet3.position - planet2.position
    planet13PosOffset = planet3.position - planet1.position
    
    f12_theta = math.atan2(planet12PosOffset.y, planet12PosOffset.x)
    f23_theta = math.atan2(planet23PosOffset.y, planet23PosOffset.x)
    f13_theta = math.atan2(planet13PosOffset.y, planet13PosOffset.x)

   
    planet1.position = util.Vector2(
        planet1.velocity.x * t_step + planet1.position.x,
        planet1.velocity.y * t_step + planet1.position.y)
    
    planet2.position = util.Vector2(
        planet2.velocity.x * t_step + planet2.position.x, 
        planet2.velocity.y * t_step + planet2.position.y)
    
    planet3.position = util.Vector2(
        planet3.velocity.x * t_step + planet3.position.x, 
        planet3.velocity.y * t_step + planet3.position.y)

    planet1.velocity = util.Vector2(
        (f12*math.cos(f12_theta) + f13*math.cos(f13_theta))/planet1.mass*t_step + planet1.velocity.x,
        (f12*math.sin(f12_theta) + f13*math.sin(f13_theta))/planet1.mass*t_step + planet1.velocity.y)
    
    planet2.velocity = util.Vector2(
        (f12*math.cos(f12_theta + math.pi) + f23*math.cos(f23_theta))/planet2.mass*t_step + planet2.velocity.x,
        (f12*math.sin(f12_theta + math.pi) + f23*math.sin(f23_theta))/planet2.mass*t_step + planet2.velocity.y)

    planet3.velocity = util.Vector2(
        (f23*math.cos(f23_theta + math.pi) + f13*math.cos(f13_theta + math.pi))/planet3.mass*t_step + planet3.velocity.x,
        (f23*math.sin(f23_theta + math.pi) + f13*math.sin(f13_theta + math.pi))/planet3.mass*t_step + planet3.velocity.y)
   
    if i%69 ==0:
        planet1.pointer.goto(planet1.position.x,planet1.position.y)
        planet2.pointer.goto(planet2.position.x, planet2.position.y)
        planet3.pointer.goto(planet3.position.x, planet3.position.y)
        
    i+=1
