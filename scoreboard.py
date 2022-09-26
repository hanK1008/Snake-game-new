from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
with open("high_score.txt") as file:
    high_score = file.read()


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.current_high_score = int(high_score)
        self.penup()
        self.color("white")
        # self.goto(0, 280)
        self.score_string()
        self.hideturtle()

    def score_string(self):
        # self.clear()
        # self.write(arg=f"Score: {self.current_score}", move=False, align="center", font=("Arial", 12, "normal"))
        # Making constant on the TOP for alignment & font
        self.goto(0, 280)
        self.write(arg=f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(200, 280)
        self.write(arg=f"High score: {self.current_high_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        self.clear()
        if self.current_score > self.current_high_score:
            self.current_high_score = self.current_score
            with open("high_score.txt", mode='w') as file:
                file.write(f"{self.current_high_score}")

        self.current_score = 0
        self.score_string()

    def score_update(self):
        self.goto(0, 280)
        self.clear()
        self.current_score += 1
        self.score_string()
