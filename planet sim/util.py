import turtle

class Planet:
    
    def __init__(self, mass, position, velocity, color):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        
        pointer = turtle.Turtle()
        pointer.up()
        pointer.shape("circle")
        pointer.color(color)
        pointer.speed(0)
        pointer.goto(position.x, position.y)
        pointer.down()
        
        self.pointer = pointer
        
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
    
    # By Integer Only!!!
    def __div__(self, other):
        return Vector2(self.x / other, self.y / other)
