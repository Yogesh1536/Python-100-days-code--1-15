from turtle import Turtle, Screen, pen
import random
import turtle
pen1 = Turtle()
screen = Screen()
turtle.colormode(255)
pen1.shape('turtle')
# pen1.color('red')
direction = [0, 90, 180, 270, 360]
colors = ['dark red', 'dark green', 'red', 'medium violet red', 'black', 'blue', 'gold', 'dark cyan', 'indian red']

turn = random.choice(direction)


def draw_shapes():
    for _ in range(3):
        pen1.forward(100)
        pen1.right(120)
    for _ in range(4):
        pen1.color('deep sky blue')
        pen1.forward(100)
        pen1.right(90)
    for _ in range(5):
        pen1.color('yellow')
        pen1.forward(100)
        pen1.right(72)
    for _ in range(6):
        pen1.color('orange red')
        pen1.forward(100)
        pen1.right(60)
    for _ in range(7):
        pen1.color('magenta')
        pen1.forward(100)
        pen1.right(51.5)
    for _ in range(8):
        pen1.color('dark goldenrod')
        pen1.forward(100)
        pen1.right(45)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

def random_walk():

    pen1.pensize(width=5)
    pen1.forward(50)
    pen1.color(random_color())
    pen1.setheading(random.choice(direction))
    pen1.speed(speed='fastest')


angle = 0
def draw_spiral():
    pen1.circle(radius=100, extent=360)
    global angle
    angle += 2
    pen1.setheading(angle)
    pen1.color(random_color())
    pen1.speed('fastest')


for spiral in range(0, 181):
    draw_spiral()

screen.exitonclick()
