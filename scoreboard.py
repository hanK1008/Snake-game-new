from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score_string()
        self.hideturtle()

    def score_string(self):
        # self.write(arg=f"Score: {self.current_score}", move=False, align="center", font=("Arial", 12, "normal"))
        # Making constant on the TOP for alignment & font
        self.write(arg=f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.clear()
        self.current_score += 1
        self.score_string()
