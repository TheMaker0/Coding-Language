import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.tracer(50)

# Define a class for celestial bodies
class CelestialBody(turtle.Turtle):
    def __init__(self, name, radius, color):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.color(color)
        self.penup()
        self.pendown()
        self.angle = 0

    def move(self):
        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)

# Create the sun
sun = CelestialBody("Sun", 0, 'yellow')
sun.shapesize(2)  # Enlarge the sun for visibility

# Create planets
mercury = CelestialBody("Mercury", 40, 'grey')
venus = CelestialBody("Venus", 80, 'orange')
earth = CelestialBody("Earth", 100, 'blue')
mars = CelestialBody("Mars", 150, 'red')
jupiter = CelestialBody("Jupiter", 180, 'brown')
saturn = CelestialBody("Saturn", 230, 'pink')
uranus = CelestialBody("Uranus", 250, 'light blue')
neptune = CelestialBody("Neptune", 280, 'black')

# Add planets to a list
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Simulation loop
while True:
    screen.update()

    # Move the celestial bodies
    for body in planets:
        body.move()

    # Increase the angle for each planet
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005
