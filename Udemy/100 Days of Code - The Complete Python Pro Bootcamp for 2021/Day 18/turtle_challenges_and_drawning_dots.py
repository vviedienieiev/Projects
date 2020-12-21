from turtle import Turtle, Screen, done, colormode
import random

# Draw a square
"""
tim = Turtle()
for _ in range(4):
    tim.forward(100)
    tim.left(90)
done()
"""

#Draw a dashed line
"""
tim = Turtle()
for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
done()
"""

#Draw the different shapes
"""def draw_shape(n_sides = 4):
    tim = Turtle()
    angle = 360/n_sides
    for _ in range(n_sides):
        tim.forward(100)
        tim.left(angle)


for shape_sides in range (3,11):
    draw_shape(shape_sides)
done()"""


# Generate a random walk
"""directions = [0,90,180,270]
tim = Turtle()
for _ in range(1000):
    tim.setheading(random.choice(directions))
    tim.forward(10)
done()"""

#Generate a spirograph
"""tim = Turtle()
tim.speed("fastest")
num_circles = 100
for _ in range(num_circles):
    tim.circle(radius=100,steps=50)
    tim.left(360/num_circles)
done()"""

colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
done()