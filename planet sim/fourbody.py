import math
import turtle
import util

gravity = 10000

def distance(pointA, pointB):
    return math.sqrt((pointB.x-pointA.x)**2 + (pointB.y-pointA.y)**2)

def grav_mag(planetA, planetB):
    return gravity*planetA.mass*planetB.mass/distance(planetA.position, planetB.position)**2

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-300,-300,300, 300)

t_step = .001

planet1 = util.Planet(120, util.Vector2(-100, 100), util.Vector2(50, -50), "green")
planet2= util.Planet(120, util.Vector2(100, 100), util.Vector2(-50, 50), "red")
planet3 = util.Planet(120, util.Vector2(100, -100), util.Vector2(50, 50), "blue")
planet4 = util.Planet(120, util.Vector2(-100, -100), util.Vector2(-50, -50), "purple")

i=0

while True:
    f12 = grav_mag(planet1, planet2)
    f23 = grav_mag(planet2, planet3)
    f13 = grav_mag(planet1, planet3)
    f14 = grav_mag(planet1, planet4)
    f24 = grav_mag(planet2, planet4)
    f34 = grav_mag(planet3, planet4)

    planet12PosOffset = planet2.position - planet1.position
    planet23PosOffset = planet3.position - planet2.position
    planet13PosOffset = planet3.position - planet1.position
    planet14PosOffset = planet4.position - planet1.position
    planet24PosOffset = planet4.position - planet2.position
    planet34PosOffset = planet4.position - planet3.position

    f12_theta = math.atan2(planet12PosOffset.y, planet12PosOffset.x)
    f23_theta = math.atan2(planet23PosOffset.y, planet23PosOffset.x)
    f13_theta = math.atan2(planet13PosOffset.y, planet13PosOffset.x)
    f14_theta = math.atan2(planet14PosOffset.y, planet14PosOffset.x)
    f24_theta = math.atan2(planet24PosOffset.y, planet24PosOffset.x)
    f34_theta = math.atan2(planet34PosOffset.y, planet34PosOffset.x)
   
    planet1.position = util.Vector2(
        planet1.velocity.x * t_step + planet1.position.x,
        planet1.velocity.y * t_step + planet1.position.y)
    
    planet2.position = util.Vector2(
        planet2.velocity.x * t_step + planet2.position.x, 
        planet2.velocity.y * t_step + planet2.position.y)
    
    planet3.position = util.Vector2(
        planet3.velocity.x * t_step + planet3.position.x, 
        planet3.velocity.y * t_step + planet3.position.y)
    
    planet4.position = util.Vector2(
        planet4.velocity.x * t_step + planet4.position.x, 
        planet4.velocity.y * t_step + planet4.position.y)

    planet1.velocity = util.Vector2(
        (f12*math.cos(f12_theta) + f13*math.cos(f13_theta) + f14*math.cos(f14_theta))/planet1.mass*t_step + planet1.velocity.x,
        (f12*math.sin(f12_theta) + f13*math.sin(f13_theta) + f14*math.sin(f14_theta))/planet1.mass*t_step + planet1.velocity.y)
    
    planet2.velocity = util.Vector2(
        (f12*math.cos(f12_theta + math.pi) + f23*math.cos(f23_theta) + f24*math.cos(f24_theta))/planet2.mass*t_step + planet2.velocity.x,
        (f12*math.sin(f12_theta + math.pi) + f23*math.sin(f23_theta) + f24*math.sin(f24_theta))/planet2.mass*t_step + planet2.velocity.y)

    planet3.velocity = util.Vector2(
        (f23*math.cos(f23_theta + math.pi) + f13*math.cos(f13_theta + math.pi) + f34*math.cos(f34_theta))/planet3.mass*t_step + planet3.velocity.x,
        (f23*math.sin(f23_theta + math.pi) + f13*math.sin(f13_theta + math.pi) + f34*math.sin(f34_theta))/planet3.mass*t_step + planet3.velocity.y)
    
    planet4.velocity = util.Vector2(
        (f14*math.cos(f14_theta + math.pi) + f24*math.cos(f13_theta + math.pi) + f34*math.cos(f34_theta + math.pi))/planet4.mass*t_step + planet4.velocity.x,
        (f14*math.sin(f14_theta + math.pi) + f24*math.sin(f13_theta + math.pi) + f34*math.sin(f34_theta + math.pi))/planet4.mass*t_step + planet4.velocity.y)
   
    if i%69 ==0:
        planet1.pointer.goto(planet1.position.x,planet1.position.y)
        planet2.pointer.goto(planet2.position.x, planet2.position.y)
        planet3.pointer.goto(planet3.position.x, planet3.position.y)
        planet4.pointer.goto(planet4.position.x, planet4.position.y)
        
    i+=1
