from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_start()


    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)