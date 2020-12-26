from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()
        self.increase_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}; Highest score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()